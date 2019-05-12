import requests
from pprint import pprint


URI = 'https://api.telegram.org/bot883808686:AAHev-RK_oBfpk-juuTf64YfR7MlUJ7eauo/getUpdates'

response = requests.get(URI)
#print(response)
print(response.json())