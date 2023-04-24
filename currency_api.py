import json
import requests

url = 'https://api.exchangerate.host/convert?from=USD&to=RUB&amount=10'
response = requests.get(url)
data = response.json()

print(data['result'])



# import requests
# import json

# url = 'https://api.exchangerate.host/convert?from=USD&to=RUB'
# response = requests.get(url)
# data = response.json()

# print(data['info']['rate'])
# print(round(data['info']['rate'], 2))



# {'motd': {'msg': 'If you or your company use this project or like what we doing, please consider backing us so we can continue maintaining and evolving this project.', 'url': 'https://exchangerate.host/#/donate'}, 'success': True, 'query': {'from': 'USD', 'to': 'EUR', 'amount': 1}, 'info': {'rate': 0.910841}, 'historical': False, 'date': '2022-03-15', 'result': 0.910841}


# {'motd': {'msg': 'If you or your company use this project or like what we doing, please consider backing us so we can continue maintaining and evolving this project.', 'url': 'https://exchangerate.host/#/donate'}, 'success': True, 'query': {'from': 'USD', 'to': 'RUB', 'amount': 1}, 'info': {'rate': 109.405222}, 'historical': False, 'date': '2022-03-16', 'result': 109.405222}