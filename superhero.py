import requests


API_KEY = '2619421814940190'
superhero = ['Hulk', 'Captain America', 'Thanos']
URL = f'https://superheroapi.com/api/{API_KEY}/search/'


def smartest_superhero():
    intelligence_superhero = {}
    for name in superhero:
        r = requests.get(URL + name)
        intelligence = r.json()['results'][0]['powerstats']['intelligence']
        intelligence_superhero[name] = int(intelligence)

    for i in sorted(intelligence_superhero.items(), key=lambda para: para[1])[::-1]:
        return f'Самый умный {i[0]}'


print(smartest_superhero())
