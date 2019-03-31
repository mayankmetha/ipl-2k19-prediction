from tkinter import *

class Window(Frame):
    teams = []
    team1 = None
    team2 = None
    def __init__(self, master=None):
        Frame.__init__(self, master)               
        self.master = master
        self.populateTeamList()
        self.initWindow()

    def initWindow(self):
        self.master.title("IPL Prediction")
        self.pack(fill=BOTH,expand=1)
        teamText = Label(self,text="SELECT TEAMS")
        teamText.place(relx=0.5,rely=0.025,anchor=CENTER)
        team1 = Button(self,text="Team1",command=self.teamSelect)
        team1.place(relx=0.3,rely=0.075,anchor=CENTER)
        team1L = Label(self,text="Team1:")
        team1L.place(relx=0.60,rely=0.075,anchor=CENTER)
        team2 = Button(self,text="Team2",command=self.teamSelect)
        team2.place(relx=0.3,rely=0.15,anchor=CENTER)
        team2L = Label(self,text="Team2:")
        team2L.place(relx=0.60,rely=0.15,anchor=CENTER)

    def populateTeamList(self):
        self.teams = ['CSK','DC','KXIP','KKR','MI','RR','RCB','SRH']

    def teamSelect(self):
        win = Toplevel()
        win.wm_title("Team Select")


root = Tk()
root.geometry("500x500")
app = Window(root)
root.mainloop()