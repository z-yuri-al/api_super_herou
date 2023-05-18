import requests



url_api = 'https://akabab.github.io/superhero-api/api/all.json'
responce = requests.get(url=url_api)
responce_json = responce.json()

new_dict = {}
for heroy_dict in responce_json:
    if heroy_dict['name'] in ['Hulk', 'Captain America', 'Thanos']:
        new_dict[heroy_dict['name']] = heroy_dict['powerstats']['intelligence']
result = sorted(new_dict.items(), key=lambda x: int(x[1]), reverse=True)

print(f'Cамый умный супергерой - {result[0][0]}')











