import http.client
import json
import pandas as pd
import os
import sqlite3 as sql

trgt_compet_szn = ['Premier League', 'England', 2023]
file_name = 'API/compet_szn.csv'

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

    if compet_name == trgt_compet_szn[0]\
        and compet_cntry == trgt_compet_szn[1]:      
        
        for szn in (compet.get('seasons')):

            szn_year = szn.get('year')

            if szn_year == trgt_compet_szn[2]:
            
                szn_year = szn.get('year')
                
                compet_szn = [compet_name] + [compet_cntry]\
                    + [szn_year] + [compet.get('league')]\
                        + [compet.get('country')] + [szn]
                
                compet_szns.loc[-1] = compet_szn
                compet_szns.index = compet_szns.index + 1
                compet_szns = compet_szns.sort_index()

compet_szns.to_csv(file_name)

# made a csv now need to do something with it

# set up db qith sqlite and either insert dataframe into a 
# table or use the csv

db_con = sql.connect("tutorial.db")

db_cur = db_con.cursor()

db_cur.execute("CREATE TABLE competition_seasons(\
               id\
               ,competition_name\
               ,competition_country_name\
               ,competition_season_year\
               ,competition\
               ,competition_country\
               ,competition_season)")

db_res = db_cur.execute("SELECT name FROM sqlite_master")
print(db_res.fetchone())
# check if file exists 
# if os.path.exists(file_name):
#     # os.remove(file_name) 

#     # Print the statement once the file is deleted  
#     print("The file: {} is deleted!".format(file_name))
# else:
#     print("The file: {} does not exist!".format(file_name))