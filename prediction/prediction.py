import os
import numpy as np
import pandas as pd
from random import randint,uniform

first = None
teams = []
batProb = None
bowlProb = None
batCluster = None
bowlCluster = None
innings1 = [0,0,0,0]
innings2 = [0,0,0,0]
bat = []
bowl = []
striker = None
nStriker = None
bowler = None
ball = 0
over = 0
wickets = 0
runs = 0
nextBowler = 1
nextBat = 2

def getTeams():
    global teams
    f = open(os.getcwd()+'/../out/prediction/teams','r')
    [teams.append(_.strip()) for _ in f.readlines()]
    f.close()

def getToss():
    global first, teams
    f = open(os.getcwd()+'/../out/prediction/toss','r')
    tmp = [_.strip() for _ in f.readlines()]
    f.close()
    if tmp[1] == 'FIELD':
        if tmp[0] == teams[0]:
            first = 1
        else:
            first = 0
    else:
        if tmp[0] == teams[0]:
            first = 0
        else:
            first = 1

def loadDatasets():
    global batProb, bowlProb, batCluster, bowlCluster
    batProb = pd.read_csv(os.getcwd()+'/../out/pvp/runsProb')
    bowlProb = pd.read_csv(os.getcwd()+'/../out/pvp/wicketsProb')
    batCluster = pd.read_csv(os.getcwd()+'/../out/clustering/bat',sep = ':', header = None, names = ['batsmen','cluster'])
    bowlCluster = pd.read_csv(os.getcwd()+'/../out/clustering/bowl',sep = ':', header = None, names = ['bowler','cluster'])

def populateTeams(x):
    global bat, bowl
    bat = []
    bowl = []
    if x == 0:
        f = open(os.getcwd()+'/../out/prediction/team0BattingOrder','r')
        [bat.append(_.strip()) for _ in f.readlines()]
        f.close()
        f = open(os.getcwd()+'/../out/prediction/team1BowlingOrder','r')
        [bowl.append(_.strip()) for _ in f.readlines()]
        f.close()
    else:
        f = open(os.getcwd()+'/../out/prediction/team1BattingOrder','r')
        [bat.append(_.strip()) for _ in f.readlines()]
        f.close()
        f = open(os.getcwd()+'/../out/prediction/team0BowlingOrder','r')
        [bowl.append(_.strip()) for _ in f.readlines()]
        f.close()

def init():
    global striker,nStriker, bowler, ball, over, wicket, runs, bat, bowl, nextBowler, nextBat
    striker = bat[0]
    nStriker = bat[1]
    nextBat = 2
    bowler = bowl[0]
    nextBowler = 1
    ball = 0
    over = 0
    wicket = 0
    runs = 0

def simulate(x,fileName):
    global striker,nStriker, bowler, ball, over, wicket, runs, bat, bowl, nextBowler, nextBat
    global batProb, bowlProb, batCluster, bowlCluster, innings1
    b1Out = 1.0
    b2Out = 1.0
    wicketProb = 0.0
    out = 0
    score = 0
    batC = 0
    bowlerC = 0
    outFile = open(fileName,'w')
    columns = ['over','ball','runs','wickets','action','striker','non-striker','bowler']
    outFile.write(",".join(columns)+"\n")
    while over != 20:
        # get cluster data
        bowlerC = [_ for _ in bowlCluster[bowlCluster['bowler'] == bowler].cluster][0]
        batC = [_ for _ in batCluster[batCluster['batsmen'] == striker].cluster][0]
        # get wicket probability
        try:
            pd.set_option('mode.chained_assignment', None)
            wicketProb = [_ for _ in bowlProb[(bowlProb['batsmen'] == batC) & (bowlProb['bowler'] == bowlerC)].wickets][0]
            wicketProb = wicketProb*0.1
        except:
            wicketProb = uniform(0, 0.25)
        # compute probability of striker/b1 getting out
        if ball == 0:
            b1Out = b1Out*(1.0-wicketProb)
        else:
            b1Out = b1Out-wicketProb
        # check if player can be made out
        if b1Out < 0.5:
            out = 1
        # batsmen action
        if out == 1:
            # make striker out
            outFile.write(str(over)+","+str(ball)+","+str(runs)+","+str(wicket)+",out,"+striker+","+nStriker+","+bowler+"\n")
            b1Out = 1.0
            wicket += 1
            if wicket == 10:
                break
            striker = bat[nextBat]
            nextBat = (nextBat + 1)%len(bat)
            out = 0
        else:
            #score runs here
            scores = batProb.loc[(batProb['batsmen'] == batC) & (batProb['bowler'] == bowlerC) & (batProb['delivery'] == (ball+1))]
            scores.drop(columns=['batsmen','bowler','delivery','balls'],inplace=True)
            try :
                score = int([_ for _ in scores.idxmax(axis=1)][0].replace('s',''))
            except:
                score = randint(0, 6)
            runs += score
            outFile.write(str(over)+","+str(ball)+","+str(runs)+","+str(wicket)+",scored "+str(score)+","+striker+","+nStriker+","+bowler+"\n")
            # swap striker and non-striker on odd score
            if (score == 1) | (score == 3) | (score == 5):
                b1Out, b2Out = b2Out, b1Out
                striker, nStriker = nStriker, striker
        # innings2 stop condition if score is greater
        if x == 1:
            if runs > innings1[0]:
                 break
        # update ball
        ball += 1
        # if ball becomes 6 or greater update over
        if ball >= 6:
            ball = 0
            over += 1
            b1Out, b2Out = b2Out, b1Out
            striker, nStriker = nStriker, striker
            bowler = bowl[nextBowler]
            nextBowler = (nextBowler + 1)%len(bowl)
    outFile.close()
    return (runs,wicket,over,ball)

getTeams()
getToss()
loadDatasets()

folderName = os.getcwd()+"/../results/"+""+teams[0]+"vs"+teams[1]+""
os.mkdir(folderName)

populateTeams(0)
init()
innings1 = simulate(0,folderName+"/innings1")

populateTeams(1)
init()
innings2 = simulate(1,folderName+"/innings2")

outFile = open(folderName+"/scorecard","w")
winnerFile = open(folderName+"/winner","w")
outFile.write("Team,Score,Overs\n")
if first == 0:
    outFile.write(teams[0]+","+str(innings1[0])+"/"+str(innings1[1])+","+str(innings1[2])+"."+str(innings1[3])+"\n")
    outFile.write(teams[1]+","+str(innings2[0])+"/"+str(innings2[1])+","+str(innings2[2])+"."+str(innings2[3])+"\n")
    if innings1[0]==innings2[0]:
        winnerFile.write("DRAW")
    elif innings1[0]>innings2[0]:
        winnerFile.write(teams[0])
    else:
        winnerFile.write(teams[1])
else:
    outFile.write(teams[1]+","+str(innings1[0])+"/"+str(innings1[1])+","+str(innings1[2])+"."+str(innings1[3])+"\n")
    outFile.write(teams[0]+","+str(innings2[0])+"/"+str(innings2[1])+","+str(innings2[2])+"."+str(innings2[3])+"\n")
    if innings1[0]==innings2[0]:
        winnerFile.write("DRAW")
    elif innings1[0]>innings2[0]:
        winnerFile.write(teams[1])
    else:
        winnerFile.write(teams[0])
outFile.close()
winnerFile.close()

exit(1)