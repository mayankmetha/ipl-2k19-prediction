import requests
from bs4 import BeautifulSoup
import os

ses = requests.Session()


def extractData(name,team,url):
    base = './PlayerStatsCricInfo/'
    batpath = base+'bat/'+team+'/'+name+'.csv'
    bowlpath = base+'bowl/'+team+'/'+name+'.csv'
    page = ses.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    table = soup.find_all('table')
    bat = open(batpath,'w')
    bowl = open(bowlpath,'w')
    try:
        for row in table[0].find('thead').find_all('tr'):
            text = []
            for cell in row.find_all('th'):
                text.append(cell.getText())
            bat.write(",".join(text)+"\n")
        for row in table[0].find('tbody').find_all('tr'):
            text = []
            for cell in row.find_all('td'):
                text.append(cell.getText())
            bat.write(",".join(text)+"\n")
        for row in table[1].find('thead').find_all('tr'):
            text = []
            for cell in row.find_all('th'):
                text.append(cell.getText())
            bowl.write(",".join(text)+"\n")
        for row in table[1].find('tbody').find_all('tr'):
            text = []
            for cell in row.find_all('td'):
                text.append(cell.getText())
            bowl.write(",".join(text)+"\n")
    except:
        print("No data found")
    bat.close()
    bowl.close()

total = 0
for files in os.listdir(os.getcwd()+'./PlayerInfo'):
    fin = open(os.getcwd()+'./PlayerInfo/'+files,'r')
    i = 1
    for lines in fin.readlines():
        s = lines.strip().split(",")
        total += 1
        print("%03d:%s:%02d:%s:%s"%(total,files,i,s[0],s[1]))
        extractData(s[0],files,s[1])
        i += 1
    fin.close()