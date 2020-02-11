import requests
import json
import random
import string
from tqdm import tqdm


def lerp(val, in_min, in_max, out_min, out_max):
    return ((val - in_min) / (in_max-in_min)) * (out_max-out_min) + out_min

# get teams in premier league (id=2)
'''url = "https://api-football-v1.p.rapidapi.com/v2/teams/league/2"

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "bf5d03e644mshee39c102c1edd31p1f825bjsne2fe296b6f94"
    }

response = requests.request("GET", url, headers=headers)
data_retrieved = response.json()

filename = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
with open(filename+'.json', 'w') as f:
    json.dump(data_retrieved, f)'''

# get athletes in premier league teams
'''with open('PremierLeagueTeams.json', 'r') as f:
    json_data = json.load(f)
    
for i in tqdm(json_data['api']['teams']):
    # print(i['team_id'], i['name'])
    team_id = i['team_id']
    url = "https://api-football-v1.p.rapidapi.com/v2/players/team/" + str(team_id)

    headers = {
        'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
        'x-rapidapi-key': "bf5d03e644mshee39c102c1edd31p1f825bjsne2fe296b6f94"
    }

    response = requests.request("GET", url, headers=headers)
    data_retrieved = response.json()

    filename = 'Athletes by team/' + i['name']
    with open(filename + '.json', 'w') as f:
        json.dump(data_retrieved, f)'''

# get premier league fixtures
'''url = "https://api-football-v1.p.rapidapi.com/v2/fixtures/league/2"

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "bf5d03e644mshee39c102c1edd31p1f825bjsne2fe296b6f94"
    }

response = requests.request("GET", url, headers=headers)
data_retrieved = response.json()

with open('PremierLeagueFixtures.json', 'w') as f:
    json.dump(data_retrieved, f)'''

# list all Chelsea players played in the 2018-2019 season
'''with open('PremierLeagueTeams.json', 'r') as f:
    json_data = json.load(f)

teams = []
for i in tqdm(json_data['api']['teams']):
    # print(i['team_id'], i['name'])
    teams.append(i['name'])

gks = []
defs = []
mids = []
atks = []

for i in teams:
    with open('Athletes by team/'+i+'.json', 'r') as f:
        json_data = json.load(f)

    for j in json_data['api']['players']:
        if j['season'] == '2018-2019' and j['league'] == 'Premier League':
            if j['rating'] != None:
                if j['position'] == 'Goalkeeper':
                    gks.append(j['rating'])
                elif j['position'] == 'Defender':
                # print(j['rating'] + '\t\t\t' + j['player_name'] + '\t\t\t' + j['team_name'])
                    defs.append(j['rating'])
                elif j['position'] == 'Midfielder':
                    mids.append(j['rating'])
                elif j['position'] == 'Attacker':
                    atks.append(j['rating'])


print('gks', min(gks), max(gks), lerp(float(min(gks)), float(min(gks)), float(max(gks)), 4, 7), lerp(float(max(gks)), float(min(gks)), float(max(gks)), 4, 7))
print('defs', min(defs), max(defs), str((float(min(defs)) - 5)*1.35 + 5), str((float(max(defs)) - 5)*1.35 + 5))
print('mids', min(mids), max(mids), str((float(min(mids)) - 5)*1.7 + 5), str((float(max(mids)) - 5)*1.7 + 5))
print('atks', min(atks), max(atks), str((float(min(atks)) - 5)*1.7 + 5), str((float(max(atks)) - 5)*1.7 + 5))'''

with open('PremierLeagueFixtures.json', 'r') as f:
    json_data = json.load(f)


