# Source Data

So just by googling open source football data quite a few come up including statsbombpy, football.db, football-data.org and API-football. I think the main this i want to seee is how easy it is to filter down to a single competition(league + season).

## Statsbombpy
So this ended up being quite simple. Firsly, this is a python package that can be stored and then it seems like you use built in fucntions to query the API. You can be pay statsbomb to access a large amount of data but without authentication you still have access to their open data source. 

To install you simple run the following command
```python
pip install statsbombpy
```

and now you're ready to get started.

In your python file you will want to import a file called sb as so

sb has a collection of functions which can be used to return different available datasets.
The functions are competitions(), matches(), lineups(), events() and competition_events() - there are more but these are the main ones - and they are all quite self explanatory and returns a dataframe which is much appreciated. For my goal of filtering to a single competition I would get I would only need to use competitions()

To workout how to filter down to a specific competition I first needed to know which fields I had available.

```python
from statsbombpy import sb

competitions_df = sb.competitions()

print(competitions_df.columns.values)
```

```
>>>['competition_id', 'season_id', 'country_name', 'competition_name', 'competition_gender', 'competition_youth', 'competition_international', 'season_name', 'match_updated', 'match_updated_360', 'match_available_360', 'match_available']
```

It looked like competition in this dataset resembled my interpretation of a league and didn't provide any context so I needed to inspect competition_name and season_name to have a better idea of what competition I would actually be selecting.

```python
from statsbombpy import sb

competitions_df = sb.competitions()

print(competitions_df[['competition_name','season_name']].sort_values(by='season_name'))
```

```
>>>          competition_name season_name
35          FIFA World Cup        1958
34          FIFA World Cup        1962
33          FIFA World Cup        1970
20        Champions League   1970/1971
19        Champions League   1971/1972
..                     ...         ...
57                 Ligue 1   2022/2023
60     Major League Soccer        2023
70       Women's World Cup        2023
2   African Cup of Nations        2023
0            1. Bundesliga   2023/2024
```

This result opened my eyes to a couple things. By using this dataset the only league available from the most recent season is the German top flight and when looking for the previous 1. Bundesliga season - 2022/2023 - I receive an error.

```python
from statsbombpy import sb

competitions_df = sb.competitions()

bundesligas_df = competitions_df[(competitions_df['competition_name'] == "1. Bundesliga")]\
                                    [['competition_id','competition_name', 'season_name']]

print(bundesligas_df)
```

So although we can filter down a single competition (league + season) with a function call and some simple dataframe stuffs it appears the availability of data isn't phenomenal.

## API -Football

