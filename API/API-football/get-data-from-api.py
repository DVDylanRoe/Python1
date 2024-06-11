import http.client
import json

conn = http.client.HTTPSConnection("v3.football.api-sports.io")

headers = {
    'x-rapidapi-host': "v3.football.api-sports.io",
    'x-rapidapi-key': "9b8d69cb9726a4743b2ffff2a71b604a"
    }

conn.request("GET", "/leagues", headers=headers)

res = conn.getresponse()
data = res.read().decode("utf-8")

compet_data = json.loads(data) #compet = competitions

#print(compet_data.keys())
# >>>dict_keys(['get', 'parameters', 'errors', 'results', 'paging', 'response'])

#inspect each key
#first get?

# compet_data_get = compet_data.get('get')
# print(compet_data_get)
# >>>competues
# looks like get returns the "table" you've requested as seen on line12

# next parameters
# compet_data_params = compet_data.get('parameters')
# print(compet_data_params)
# >>> []
# empty? bcos i didnt use any looks like on line 12 i'd have to do something like "/competues?parameter=value"

# next errors
# compet_data_errs = compet_data.get('errors')
# print(compet_data_errs)
# >>> []
# also empty but we had no errors maybe for a failed request this is where you can find an error message rather than the script failing

# next results
# compet_data_rs = compet_data.get('results')
# print(compet_data_rs)
# >>>1112
# my best guess is how many results are returned

# next paging
# compet_data_pg = compet_data.get('paging')
# print(compet_data_pg)
# >>>{'current': 1, 'total': 1}
# think it does what it says - will be interested to see what happens when toal > 1

# finally response
compet_data_rsp = compet_data.get('response') #re = response
# print(compet_data_rsp)
# this is where the money is

# is it another dictionary
# print(type(compet_data_rsp))
# >>><class 'list'>
# nope it's a list

# ...of length?
# print(len(compet_data_rsp))
# >>>1112
# thats the same as results
# my best guess is there are 1112 competues in this dataset

# lets look at element 1
# print(compet_data_rsp[0])
# print(type(compet_data_rsp[0]))
# >>><class 'dict'>
# it's a dictionary

#what keys does it have
# item2 = compet_data_rsp[0]
# print(item2)

# print(item2.keys())
# competue coutnry and compet_szns

# inspect each key
# value2 = item2.get('league')
# print(value2)
# another dictionary with id,name, type and logo

# inspect each key
# value2 = item2.get('country')
# print(value2)
# another dictionary with name, code and flag
# would need id from competue to tie it to anything

# inspect each key
# value2 = item2.get('seasons')
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
#         b = a['seasons']
#         for c in b:
#                 d = c['year']
#                 print(d)

# years = [compet_szn['year'] for competition in value1 for compet_szn in competition['seasons']]

# print(years)

compet_szns = []
for compet in compet_data_rsp: #A[i]
    if compet.get('league').get('id') == 39: 
        compet_id = [compet.get('league').get('name')]
        compet_cntry = [compet.get('country').get('name')]
        for szn in (compet.get('seasons')):
            szn_year = szn.get('year')
            # if compet_szn_year >= 2022:
                # compet_id = [compet.get('league').get(key) for key in ['id', 'name', 'type']] #A[i][B][C]
                # compet_key = compet_id + [compet.get(key) for key in ['year','start', 'end']]
                # compet_keys += [compet_key]                
            compet_szn = compet_id + compet_cntry + [szn_year]
            compet_szns += [compet_szn]

print(compet_szns)

# i have successfully idenfitied a way to isolate unique competitions with this api