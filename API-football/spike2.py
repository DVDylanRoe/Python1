import requests

url = "https://v3.football.api-sports.io/leagues"

payload={}
headers = {
  'x-rapidapi-key': '9b8d69cb9726a4743b2ffff2a71b604a',
  'x-rapidapi-host': 'v3.football.api-sports.io'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)