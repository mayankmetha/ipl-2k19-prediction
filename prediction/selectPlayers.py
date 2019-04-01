#!/usr/bin/python3

# imports
import os
from tkinter import Tk,Button,Label,Radiobutton,Listbox,Toplevel,IntVar,CENTER,MULTIPLE,END,DISABLED,NORMAL

# global variables
teams = ['CSK','DC','KXIP','KKR','MI','RR','RCB','SRH']
team = []
team1S = []
team2S = []
team1P = []
team2P = []
teamVar = None
win = None
team1L = None
team2L = None
team1 = None
team2 = None
root = None
lb = None
teamB1 = None
teamB2 = None
i = 0

# root frame
def main():
    global root
    global team1
    global team2
    global team1L
    global team2L
    root.geometry("500x300")
    root.title("IPL Prediction Step1")
    teamText = Label(root,text="SELECT TEAMS")
    teamText.pack()
    teamText.place(relx=0.5,rely=0.05,anchor=CENTER)
    team1 = Button(root,text="Team1",command=teamSelect)
    team1.pack()
    team1.place(relx=0.3,rely=0.15,anchor=CENTER)
    team1L = Label(root,text="Team1:")
    team1L.pack()
    team1L.place(relx=0.60,rely=0.15,anchor=CENTER)
    team2 = Button(root,text="Team2",command=teamSelect)
    team2.pack()
    team2.place(relx=0.3,rely=0.3,anchor=CENTER)
    team2L = Label(root,text="Team2:")
    team2L.pack()
    team2L.place(relx=0.60,rely=0.3,anchor=CENTER)
    
# read dataset data
def readTeamFile(team):
    l = []
    fin = open(os.getcwd()+'/../datasets/teamList/'+team,'r')
    for line in fin.readlines():
        s = line.split(",")
        l.append(s[1])
    fin.close()
    return l

# team select window
def teamSelect():
    global teamVar
    global win
    win = Toplevel()
    win.wm_title("Team")
    teamVar = IntVar()
    teamVar.set(0)
    i = 0
    for t in teams:
        tmp = Radiobutton(win,indicatoron = 0,width=20,text=t,variable=teamVar,value=i,command=updateTeams)
        tmp.pack()
        i += 1

# update team label after selection
def updateTeams():
    global team
    global teams
    global team1L
    global team2L
    global win
    global teamVar
    global team1
    global team2
    global team1S
    global team2S
    team.append(teams[teamVar.get()])
    teams.remove(teams[teamVar.get()])
    win.destroy()
    try:
        str1 = "Team1: "+team[0]
        team1L.configure(text=str1)
        team1L.pack()
        team1L.place(relx=0.60,rely=0.15,anchor=CENTER)
        team1.configure(state=DISABLED)
        team1.pack()
        team1.place(relx=0.3,rely=0.15,anchor=CENTER)
        team1S = readTeamFile(team[0])
        teamFunction(0,team1S)
    except:
        pass
    try:
        str2 = "Team2: "+team[1]
        team2L.configure(text=str2)
        team2L.pack()
        team2L.place(relx=0.60,rely=0.3,anchor=CENTER)
        team2.configure(state=DISABLED)
        team2.pack()
        team2.place(relx=0.3,rely=0.3,anchor=CENTER)
        team2S = readTeamFile(team[1])
        teamFunction(1,team2S)
    except:
        pass

# buttons for playing 11 selection
def teamFunction(index,t):
    global root
    global teamB1
    global teamB2
    teamSelectionText = Label(root,text="SELECT PLAYING 11 FOR "+team[index])
    teamSelectionText.pack()
    if index == 0:
        teamSelectionText.place(relx=0.5,rely=0.50,anchor=CENTER)
    else:
        teamSelectionText.place(relx=0.5,rely=0.70,anchor=CENTER)
    if index == 0:
        teamB1 = Button(root,text=team[index]+" PLAYING 11",width=30,command=lambda:selectPlayingSquad(index,t))
        teamB1.pack()
        teamB1.place(relx=0.5,rely=0.60,anchor=CENTER)
    else:
        teamB2 = Button(root,text=team[index]+" PLAYING 11",width=30,command=lambda:selectPlayingSquad(index,t))
        teamB2.pack()
        teamB2.place(relx=0.5,rely=0.80,anchor=CENTER)

# window for playing 11 selection
def selectPlayingSquad(index,t):
    global win
    global b
    global lb
    win = Toplevel()
    win.wm_title(team[index])
    lb = Listbox(win,selectmode=MULTIPLE,height=len(t))
    for x in t:
        lb.insert(END,x.strip())
    lb.pack()
    lb.bind("<<ListboxSelect>>",buttonStateToggle)
    b = Button(win,text="OK",state=DISABLED,command=lambda:playingSquad(index))
    b.pack()

# saving playing 11
def playingSquad(index):
    global win
    global lb
    global team1P
    global team2P
    global i
    global teamB1
    global teamB2
    if index == 0:
        team1P = [lb.get(idx) for idx in lb.curselection()]
        i += 1
        teamB1.configure(state=DISABLED)
        teamB1.pack()
        teamB1.place(relx=0.5,rely=0.6,anchor=CENTER)
    elif index == 1:
        team2P = [lb.get(idx) for idx in lb.curselection()]
        i += 1
        teamB2.configure(state=DISABLED)
        teamB2.pack()
        teamB2.place(relx=0.5,rely=0.8,anchor=CENTER)
    win.destroy()
    if i == 2:
        goNext()

# toggle ok button in playing 11 selection window
def buttonStateToggle(a):
    global b
    global lb
    if len(lb.curselection()) == 11:
        b.configure(state=NORMAL)
        b.pack()
    else:
        b.configure(state=DISABLED)
        b.pack()

# save state and exit process
def goNext():
    global root
    fout = open(os.getcwd()+'/../out/prediction/teams','w')
    for _ in team:
        fout.write(_+"\n")
    fout.close()
    fout = open(os.getcwd()+'/../out/prediction/team0','w')
    for _ in team1P:
        fout.write(_+"\n")
    fout.close()
    fout = open(os.getcwd()+'/../out/prediction/team1','w')
    for _ in team2P:
        fout.write(_+"\n")
    fout.close()
    exit(1)
    
# global execution
root = Tk()
main()
root.mainloop()