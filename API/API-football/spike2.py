import http.client
import json
import pandas as pd
import os

trgt_compet_szn = ['Premier League', 'England', 2013]
file_name = 'compet_szn.csv'

conn = http.client.HTTPSConnection("v3.football.api-sports.io")

headers = {
    'x-rapidapi-host': "v3.football.api-sports.io",
    'x-rapidapi-key': "9b8d69cb9726a4743b2ffff2a71b604a"
    }

conn.request("GET", "/leagues", headers=headers)

res = conn.getresponse()
data = res.read().decode("utf-8")

compet_data = json.loads(data) # compet = competitions

compet_data_rsp = compet_data.get('response') # rsp = response

compet_szns = pd.DataFrame(
    columns = ['competition_name', 'competition_country_name'\
               ,'competition_season_year', 'competition'\
               ,'competition_country', 'competition_season'] 
)

for compet in compet_data_rsp: 
       
    compet_name = compet.get('league').get('name')
    compet_cntry = compet.get('country').get('name') # cntry = country

    if compet_name == trgt_compet_szn[0] and compet_cntry == trgt_compet_szn[1]:      
        
        for szn in (compet.get('seasons')):
            
            szn_year = szn.get('year')
              
            compet_szn = [compet_name] + [compet_cntry] + [szn_year]\
              + [compet.get('league')] + [compet.get('country')] + [szn]
            
            compet_szns.loc[-1] = compet_szn
            compet_szns.index = compet_szns.index + 1
            compet_szns = compet_szns.sort_index()

compet_szns.to_csv('API/' + file_name)

# made a csv now need to do something with it

# check if file exists 
if os.path.exists('API/' + file_name):
    os.remove('API/' + file_name) 

    # Print the statement once the file is deleted  
    print("The file: {} is deleted!".format(file_name))
else:
    print("The file: {} does not exist!".format(file_name))



