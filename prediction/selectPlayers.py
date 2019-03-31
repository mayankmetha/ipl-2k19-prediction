#!/usr/bin/python3
import os
from tkinter import *

teams = ['CSK','DC','KXIP','KKR','MI','RR','RCB','SRH']
team = []
team1S = []
team2S = []
teamVar = None
win = None
team1L = None
team2L = None
team1 = None
team2 = None
root = None

def main():
    global root
    global team1
    global team2
    global team1L
    global team2L
    root.geometry("500x500")
    root.title("IPL Prediction")
    teamText = Label(root,text="SELECT TEAMS")
    teamText.pack()
    teamText.place(relx=0.5,rely=0.025,anchor=CENTER)
    team1 = Button(root,text="Team1",command=teamSelect)
    team1.pack()
    team1.place(relx=0.3,rely=0.075,anchor=CENTER)
    team1L = Label(root,text="Team1:")
    team1L.pack()
    team1L.place(relx=0.60,rely=0.075,anchor=CENTER)
    team2 = Button(root,text="Team2",command=teamSelect)
    team2.pack()
    team2.place(relx=0.3,rely=0.15,anchor=CENTER)
    team2L = Label(root,text="Team2:")
    team2L.pack()
    team2L.place(relx=0.60,rely=0.15,anchor=CENTER)
    
def readTeamFile(team):
    l = []
    fin = open(os.getcwd()+'/../datasets/teamList/'+team,'r')
    for line in fin.readlines():
        s = line.split(",")
        l.append(s[1])
    fin.close()
    return l

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
        team1L.place(relx=0.60,rely=0.075,anchor=CENTER)
        team1.configure(state=DISABLED)
        team1.pack()
        team1.place(relx=0.3,rely=0.075,anchor=CENTER)
        team1S = readTeamFile(team[0])
        teamFunction(0,team1S)
    except:
        pass
    try:
        str2 = "Team2: "+team[1]
        team2L.configure(text=str2)
        team2L.pack()
        team2L.place(relx=0.60,rely=0.15,anchor=CENTER)
        team2.configure(state=DISABLED)
        team2.pack()
        team2.place(relx=0.3,rely=0.15,anchor=CENTER)
        team2S = readTeamFile(team[1])
        teamFunction(1,team2S)
    except:
        pass

def teamFunction(index,t):
    global root
    teamSelectionText = Label(root,text="SELECT PLAYING 11 FOR "+team[index])
    teamSelectionText.pack()
    if index == 0:
        teamSelectionText.place(relx=0.5,rely=0.215,anchor=CENTER)
    else:
        teamSelectionText.place(relx=0.5,rely=0.350,anchor=CENTER)
    teamB = Button(root,text=team[index]+" PLAYING 11",command=lambda:selectPlayingSquad(index,t))
    teamB.pack()
    if index == 0:
        teamB.place(relx=0.5,rely=0.275,anchor=CENTER)
    else:
        teamB.place(relx=0.5,rely=0.415,anchor=CENTER)

def selectPlayingSquad(index,t):
    global win
    global b
    global i
    i = 0
    win = Toplevel()
    win.wm_title(team[index])
    lb = Listbox(win,selectmode=MULTIPLE,height=len(t))
    for x in t:
        lb.insert(END,x.strip())
    lb.pack()
    b = Button(win,text="OK",state=DISABLED)
    b.pack()


root = Tk()
main()
root.mainloop()