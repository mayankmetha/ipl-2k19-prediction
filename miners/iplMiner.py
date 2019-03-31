import requests
from bs4 import BeautifulSoup
import os

baseTeamUrl = "https://www.iplt20.com"
teamUrl = []
teamAbb = ['CSK','DC','KXIP','KKR','MI','RR','RCB','SRH']

def getTeam():
    page = requests.get(baseTeamUrl+"/teams/")
    soup = BeautifulSoup(page.content, 'html.parser')
    for t in soup.find_all('a', class_="card team-card"):
        teamUrl.append(t.get('href'))

def getheaders(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    tab = soup.find_all('table', class_="table table--scroll-on-phablet player-stats-table")
    batrow = tab[0].find_all('tr')
    bowlrow = tab[1].find_all('tr')
    i = 2
    player = "Player"
    team = "Team"
    row = []
    bat = []
    for cell in batrow[0].find_all('th'):
        if i == 2:
            bat.append(team)
            bat.append(player)
            i = 1
            pass
        else:
            bat.append(str(cell.getText().replace("*","").replace(",","")))
    row.append(",".join(bat))
    bowl = []
    for cell in bowlrow[0].find_all('th'):
        if i == 1:
            bowl.append(team)
            bowl.append(player)
            i = 0
            pass
        else:
            bowl.append(str(cell.getText().replace("*","").replace(",","")))
    row.append(",".join(bowl))
    return str("#".join(row))

def getPlayerInfo(team,player,url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    tab = soup.find_all('table', class_="table table--scroll-on-phablet player-stats-table")
    row = []
    bat = []
    bowl = []
    bat.append(team)
    bat.append(player)
    bowl.append(team)
    bowl.append(player)
    try:
        batrow = tab[0].find_all('tr')
        bowlrow = tab[1].find_all('tr')
        i = 2
        for cell in batrow[1].find_all('td'):
            if i == 2:
                i = 1
                pass
            else:
                bat.append(str(cell.getText().replace("*","").replace(",","")))
        row.append(",".join(bat))
        for cell in bowlrow[1].find_all('td'):
            if i == 1:
                i = 0
                pass
            else:
                bowl.append(str(cell.getText().replace("*","").replace(",","")))
        row.append(",".join(bowl))
    except:
        for i in range(13):
            bat.append("-")
        row.append(",".join(bat))
        for i in range(10):
            bowl.append("-")
        row.append(",".join(bowl))
    return str("#".join(row))

getTeam()
fbat = open(os.getcwd()+'/../datasets/PlayerStatsIPL/bat.csv','w')
fbowl = open(os.getcwd()+'/../datasets/PlayerStatsIPL/bowl.csv','w')
flag = 1
total = 0
for files in teamAbb:
    fin = open(os.getcwd()+'/../datasets/teamList/'+files,'r')
    i = 1
    for lines in fin.readlines():
        s = lines.strip().split(",")
        url = baseTeamUrl+teamUrl[teamAbb.index(files)]+"/squad/"+s[0]+"/"+s[1].replace(" ","-")
        total +=1 
        print("%03d:%s:%02d:%s:%s"%(total,files,i,s[1],url))
        if flag == 1:
            header = getheaders(url)
            string = header.split("#")
            fbat.write(string[0]+"\n")
            fbowl.write(string[1]+"\n")
            flag = 0
        data = getPlayerInfo(files,s[1],url)
        string = data.split("#")
        fbat.write(string[0]+"\n")
        fbowl.write(string[1]+"\n")
        i += 1
    fin.close()
fbat.close()
fbowl.close()