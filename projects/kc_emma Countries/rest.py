import requests
url = 'https://restcountries.eu/rest/v2/all'
resp = requests.get(url)
data = resp.json()

print('what is your name')
user_name = input()
print('Which country are you from')
user_country = input()

for country in data:

    if country['name'].upper() == user_country.upper():
        print(f'You are welcome Mr.{user_name} from {user_country}')
        print('How is {} the capital of your country doing ' .format((country['capital'])))
        for neighbour in country['borders']:
            code = requests.get('https://restcountries.eu/rest/v2/alpha/{}'.format(neighbour)).json()
            print(code['name'])
