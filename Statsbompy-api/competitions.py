from statsbombpy import sb

competitions_df = sb.competitions()

'''
print(item1)
#looks like a dataframe I want to output a list of all headings
'''

'''
print(list(item1.columns.values))

['competition_id', 'season_id', 'country_name', 'competition_name', 'competition_gender'
, 'competition_youth', 'competition_international', 'season_name', 'match_updated'
, 'match_updated_360', 'match_available_360', 'match_available']
'''

'''
#my best guess is competition name
print(item1['competition_name'].tolist())
FA Women's Super League?
'''

'''
#so i want all the competitions where competition name is 'FA Women's Super League
print(item1[item1['competition_name'] == "FA Women's Super League" ])
returns 3 competitions each with a different season...what does season mean?

the dataframe has a field called season_name...let us inspect
print(item1[item1['competition_name'] == "FA Women's Super League" ]['season_name'])
2020/2021
2019/2020
2018/2019
'''

'''
#do any leagues have any more recent data?
print(item1[['competition_name','season_name']].sort_values(by='season_name'))
Bundesligs 2023/2024 it is
'''

competition_id = competitions_df[(competitions_df['competition_name'] == "1. Bundesliga") \
                                 & (competitions_df['season_name'] == '2023/2024')]\
                                    ['competition_id'][0].astype(int)

#now we can filter teams and games down to competitions
#or atleast one competition at a time
print(competition_id)