import http.client

import json

conn = http.client.HTTPSConnection("v3.football.api-sports.io")

headers = {
    'x-rapidapi-host': "v3.football.api-sports.io",
    'x-rapidapi-key': "9b8d69cb9726a4743b2ffff2a71b604a"
    }

conn.request("GET", "/leagues", headers=headers)

res = conn.getresponse()
data = res.read()

compet_api = json.loads(data.decode("utf-8")) #compet = competitions

#print(compet_api.keys())
# >>>dict_keys(['get', 'parameters', 'errors', 'results', 'paging', 'response'])

#inspect each key
#first get?

# value1 = compet_api.get('get')
# print(value1)
# >>>leagues
# looks like get returns the "table" you've requested as seen on line12

# next parameters
# value1 = compet_api.get('parameters')
# print(value1)
# >>> []
# empty? bcos i didnt use any looks like on line 12 i'd have to do something like "/leagues?parameter=value"

# next errors
# value1 = compet_api.get('errors')
# print(value1)
# >>> []
# also empty but we had no errors maybe for a failed request this is where you can find an error message rather than the script failing

# next results
# value1 = compet_api.get('results')
# print(value1)
# >>>1112
# my best guess is how many results are returned

# next paging
# value1 = compet_api.get('paging')
# print(value1)
# >>>{'current': 1, 'total': 1}
# think it does what it says - will be interested to see what happens when toal > 1

# finally response
compet_api_re = compet_api.get('response') #re = response
# print(compet_api_reponse)
# this is where the money is

# is it another dictionary
# print(type(compet_api_reponse))
# >>><class 'list'>
# nope it's a list

# ...of length?
# print(len(compet_api_reponse))
# >>>1112
# thats the same as results
# my best guess is there are 1112 leagues in this dataset

# lets look at element 1
# print(compet_api_reponse[0])
# print(type(compet_api_reponse[0]))
# >>><class 'dict'>
# it's a dictionary

#what keys does it have
# item2 = compet_api_reponse[0]
# print(item2)

# print(item2.keys())
# league coutnry and compet_szns

# inspect each key
# value2 = item2.get('league')
# print(value2)
# another dictionary with id,name, type and logo

# inspect each key
# value2 = item2.get('country')
# print(value2)
# another dictionary with name, code and flag
# would need id from league to tie it to anything

# inspect each key
# value2 = item2.get('compet_szns')
# print(value2)
# print(type(value2))
# a list...of dictionaries?

# inspect the list - element 1/"0"
# print(value2[0])
# yup definitely a dict
# item3 = value2[0]
# print(item3.keys())
# has 5 keys
# year(year), start(date), end(date), current(boolean), coverage(metadata dictionary)

# so I want a unique list of compet_szns accessible within this request

# for a in value1:
#         b = a['compet_szns']
#         for c in b:
#                 d = c['year']
#                 print(d)

# years = [compet_szn['year'] for competition in value1 for compet_szn in competition['compet_szns']]

# print(years)


compet_data_list = []
for compet in compet_api_re: #A[i]
    if compet.get('league').get('id') == 39: 
        compet_id = [compet.get('league').get(key) for key in ['id', 'name']]
        compet_cntry = [compet.get('country').get('name')]
        for compet_szn in (compet.get('seasons')):
            compet_szn_year = compet_szn.get('year')
            # if compet_szn_year >= 2022:      
                # compet_id = [compet.get('league').get(key) for key in ['id', 'name', 'type']] #A[i][B][C]
                # compet_data = compet_id + [compet_szn.get(key) for key in ['year','start', 'end']]
                # compet_data_list += [compet_data]                
            compet_data = compet_id + compet_cntry + [compet_szn_year]
            compet_data_list += [compet_data]

print(compet_data_list)

# i have successfully idenfitied a way to isolate unique competitions with this api

    











