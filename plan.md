# The Plan

## 1 Goals

1. want to assess team performance [ ]
    - get data in
    - model sports performance
    - build pipeline
    - analyse data
    - present analysis


## Progress

### Getting Data In

#### 2SOURCE DATA
so have two methods of getting data
- [1] statsombpy [x]
- [2] api-football [x]

now [1] is simpler (see Statsbompy-api\competitions.py) but limited data but [2] is probably going to be harder (see API-football\spike.py) in the long run but have a lot of oppurtunity to increase the size of the project

the reason [2] is trickier is because it has so much data and its stored in nested lists and dictionaries but I have two options - I think having that much more data will be better in the long run so imma use [2]

####  FILTERING COMPETITIONS
- [3] filter data before it comes in [ ]
- [4] filter data after it comes in [ ]

with [3] once again it keeps it simple but if i wanted to load multiple leagues/seasons it would require a request each and im limited to 100 requests a day

with [4] it gets a bit ugly but is doable and i could get as many leagues/seasons as i want with one request

going to try both but if [4] is simple enough i'll use that as will be beneficial long term

