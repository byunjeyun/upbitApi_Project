import pyupbit

ticker_list = pyupbit.get_tickers(fiat="KRW")
coin_list=[]
for ticker in ticker_list:
     coin_list.append(ticker[4:10])
print(coin_list)
