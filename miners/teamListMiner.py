import requests
import json

base = "https://cricketapi.platform.iplt20.com/tournaments/10192/squads/"

page = requests.get(base).text
data = json.loads(page)
for teams in data['squads']['ALL']:
    name = teams['team']['abbreviation']
    fout = open('../datasets/teamList/'+name,'w')
    for p in teams['players']:
        fout.write(str(p['id'])+","+p['fullName']+'\n')
    fout.close()
