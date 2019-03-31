import requests
from bs4 import BeautifulSoup
import os

def extractData(name,team,url):
    base = '../datasets/PlayerStatsCricInfo/'
    batpath = base+'bat/'+team+'/'+name+'.csv'
    bowlpath = base+'bowl/'+team+'/'+name+'.csv'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    table = soup.find_all('table')
    bat = open(batpath,'w')
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
    bat.close()
    bowl = open(bowlpath,'w')
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
    bowl.close()

total = 0
for files in os.listdir(os.getcwd()+'/../datasets/PlayerInfo'):
    fin = open(os.getcwd()+'/../datasets/PlayerInfo/'+files,'r')
    i = 1
    for lines in fin.readlines():
        s = lines.strip().split(",")
        total += 1
        print("%03d:%s:%02d:%s"%(total,files,i,s[0]))
        extractData(s[0],files,s[1])
        i += 1
    fin.close()