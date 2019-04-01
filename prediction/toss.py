#!/usr/bin/python3

# imports
from tkinter import Tk,Toplevel,Radiobutton,Label,IntVar,CENTER
import os

# global variables
teamList = []
choices = ['FIELD','BAT']
root = None
team = None
choice = None
var = None
l = None

# get data from files of previous process
def preprocess():
    global teamList
    fin = open(os.getcwd()+'/../out/prediction/teams','r')
    for _ in fin.readlines():
        teamList.append(_.strip())
    fin.close()

# root frame
def main():
    global root
    global teamList
    global var
    global l
    root.geometry("500x100")
    root.title("IPL Prediction Step 4")
    l = Label(root,text="TOSS WINNER")
    l.pack()
    l.place(relx=0.5,rely=0.25,anchor=CENTER)
    var = IntVar()
    var.set(0)
    i = 0
    x = 0.4
    for t in teamList:
        tmp = Radiobutton(root,indicatoron = 0,width=10,text=t,variable=var,value=i,command=selectChoice)
        tmp.pack()
        tmp.place(relx=x,rely=0.65,anchor=CENTER)
        x += 0.2
        i += 1

# toss winner options
def selectChoice():
    global var  
    global team
    global teamList
    team = teamList[var.get()]
    l.configure(text="CHOICE")
    l.pack()
    l.place(relx=0.5,rely=0.25,anchor=CENTER)
    var = IntVar()
    var.set(0)
    i = 0
    x = 0.4
    for t in choices:
        tmp = Radiobutton(root,indicatoron = 0,width=10,text=t,variable=var,value=i,command=goNext)
        tmp.pack()
        tmp.place(relx=x,rely=0.65,anchor=CENTER)
        x += 0.2
        i += 1

# save state and exit process
def goNext():
    global var  
    global choice
    global team
    global choices
    choice = choices[var.get()]
    fout = open(os.getcwd()+'/../out/prediction/toss','w')
    fout.write(team+"\n"+choice)
    fout.close()
    exit(1)

preprocess()
root = Tk()
main()
root.mainloop()