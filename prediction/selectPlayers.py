from tkinter import *

teams = ['CSK','DC','KXIP','KKR','MI','RR','RCB','SRH']
team = []
teamVar = None
win = None
team1L = None
team2L = None
team1 = None
team2 = None

def teamSelect():
    global teamVar
    global win
    win = Toplevel()
    win.wm_title("Team Select")
    win.geometry("250x200")
    teamVar = IntVar()
    teamVar.set(0)
    i = 0
    for t in teams:
        tmp = Radiobutton(win,text=t,variable=teamVar,value=i,command=updateTeams)
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
    except:
        pass

root = Tk()
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
root.mainloop()

