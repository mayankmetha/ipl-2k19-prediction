from tkinter import *
import os
import sys

root = None
team = None
teamList = []
BattingOrder = []
Bowlers = []
number = None
battingOrderButton = None
bowlerButton = None
win = None
lb = None
b = None
up = None
down = None
i = 0

def preprocess(index):
    global teamList
    global team
    fin = open(os.getcwd()+'/../out/prediction/teams','r')
    teams = []
    for _ in fin.readlines():
        teams.append(_.strip())
    team = teams[index]
    fin.close()
    if index == 0:
        files = "team0"
    else:
        files = "team1"
    fin = open(os.getcwd()+'/../out/prediction/'+files,'r')
    for _ in fin.readlines():
        teamList.append(_.strip())
    fin.close()

def main(index):
    global root
    global battingOrderButton
    global bowlerButton
    root.geometry("500x500")
    title = "IPL Prediction Step"+str(number+2)
    root.title(title)
    l1 = Label(root,text="Team "+team+"")
    l1.pack()
    l1.place(relx=0.5,rely=0.025,anchor=CENTER)
    l2 = Label(root,text="Batting order")
    l2.pack()
    l2.place(relx=0.5,rely=0.075,anchor=CENTER)
    battingOrderButton = Button(root,text="Select Batting Order",width=30,command=battingOrder)
    battingOrderButton.pack()
    battingOrderButton.place(relx=0.5,rely=0.125,anchor=CENTER)
    l3 = Label(root,text="Bowlers List")
    l3.pack()
    l3.place(relx=0.5,rely=0.200,anchor=CENTER)
    bowlerButton = Button(root,text="Select Bowlers",width=30,command=bowlerSelection)
    bowlerButton.pack()
    bowlerButton.place(relx=0.5,rely=0.250,anchor=CENTER)

def battingOrder():
    global win
    global lb
    global teamList
    global b
    win = Toplevel()
    win.wm_title("Batting Order")
    lb = Listbox(win,height=len(teamList))
    for _ in teamList:
        lb.insert(END,_)
    lb.grid(row=0,columnspan=2)
    up = Button(win, text="↑",width=5,command=upClicked)
    up.grid(row=1,column=0)
    down = Button(win, text="↓",width=5,command=downClicked)
    down.grid(row=1,column=1)
    b = Button(win, text="OK",width=15,command=ok1Clicked)
    b.grid(row=3,columnspan=2)

def upClicked():
    global lb
    try:
        idx = lb.curselection()
        if not idx:
            return
        for pos in idx:
            if pos == 0:
                continue
            text = lb.get(pos)
            lb.delete(pos)
            lb.insert(pos-1,text)
            lb.selection_set(pos-1)
    except:
        pass

def downClicked():
    global lb
    try:
        idx = lb.curselection()
        if not idx:
            return
        for pos in idx:
            if pos == lb.size()-1:
                continue
            text = lb.get(pos)
            lb.delete(pos)
            lb.insert(pos+1,text)
            lb.selection_set(pos+1)
    except:
        pass

def ok1Clicked():
    global i
    global win
    global lb
    global battingOrderButton
    global BattingOrder
    global b
    for _ in lb.get(0,END):
        BattingOrder.append(_)
    i += 1
    battingOrderButton.configure(state=DISABLED)
    battingOrderButton.pack()
    battingOrderButton.place(relx=0.5,rely=0.125,anchor=CENTER)
    goNext()
    win.destroy()

def bowlerSelection():
    global win
    global lb
    global teamList
    global b
    win = Toplevel()
    win.wm_title("Bowlers")
    lb = Listbox(win,selectmode=MULTIPLE,height=len(teamList))
    for _ in teamList:
        lb.insert(END,_)
    lb.pack()
    b = Button(win, text="OK",command=ok2Clicked)
    b.pack()

def ok2Clicked():
    global i
    global win
    global lb
    global bowlerButton
    global Bowlers
    global b
    Bowlers = [lb.get(idx) for idx in lb.curselection()]
    i += 1
    if len(Bowlers) == 0:
        pass
    else:
        bowlerButton.configure(state=DISABLED)
        bowlerButton.pack()
        bowlerButton.place(relx=0.5,rely=0.250,anchor=CENTER)
        goNext()
    win.destroy()

def goNext():
    global i
    global number
    global Bowlers
    global BattingOrder
    if i != 2:
        return
    fout = open(os.getcwd()+'/../out/prediction/team'+str(number)+'BattingOrder','w')
    for _ in BattingOrder:
        fout.write(_+"\n")
    fout.close()
    fout = open(os.getcwd()+'/../out/prediction/team'+str(number)+'Bowlers','w')
    for _ in Bowlers:
        fout.write(_+"\n")
    fout.close()
    exit(1)

number = int(sys.argv[1])
preprocess(number)
root = Tk()
main(number)
root.mainloop()