import http.client
import json
import time

conn = http.client.HTTPSConnection("v3.football.api-sports.io")

headers = {
    'x-rapidapi-host': "v3.football.api-sports.io",
    'x-rapidapi-key': "9b8d69cb9726a4743b2ffff2a71b604a"
    }

conn.request("GET", "/leagues", headers=headers)

res = conn.getresponse()
data = res.read().decode("utf-8")

compet_data = json.loads(data) #compet = competitions

compet_data_rsp = compet_data.get('response') #re = response

for compet in compet_data_rsp:
    compet_leag = compet.get('league')
    compet_leag_name = compet_leag.get('name')
    compet_cntry = compet.get('country')
    compet_cntry_name = compet_cntry.get('name')

    if compet_leag_name == "Premier League" \
        and compet_cntry_name == "England":
            compet_id = compet_leag.get('id')
            compet_szns = compet.get('seasons')

            compet_szn_years = [compet_szn.get('year') for compet_szn in compet_szns ]
            compet_szn_year = max(compet_szn_years)

# ?season=2019&team=33&league=39

conn.request("GET", "/teams?season=" + str(compet_szn_year) + "&league=" + str(compet_id), headers=headers)

res = conn.getresponse()
data = res.read()

club_data = json.loads(data)

club_data_rsp = club_data.get('response')

club_ids = []

for club in club_data_rsp:

    club_team = club.get('team')
    club_team_id = club_team.get('id')
    club_ids += [club_team_id]

for club_id in club_ids:
    
    conn.request("GET", "/teams/statistics?season=" + str(compet_szn_year) + "&team=" + str(club_id) + "&league=" + str(compet_id), headers=headers)

    res = conn.getresponse()
    data = res.read()

    club_stats_data = json.loads(data)

    club_stats_data_rsp = club_stats_data.get('response')

    print(club_stats_data)

    time.sleep(6) # limited to 10 requests a minute

    