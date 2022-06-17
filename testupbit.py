import requests

url = "https://api.upbit.com/v1/ticker"

param = {"markets":"KRW-BTC"}
headers = {"Accept": "application/json"}

response = requests.get(url, params=param)
upbitresult = response.json()
print(upbitresult[0]['market'])
print(upbitresult[0]['trade_price'])
print(upbitresult[0]['signed_change_rate'])
print(upbitresult[0]['acc_trade_volume_24h'])
print(upbitresult[0]['highest_52_week_price'])
print(upbitresult[0]['lowest_52_week_price'])
print(upbitresult[0]['high_price'])
print(upbitresult[0]['low_price'])
print(upbitresult[0]['prev_closing_price'])

