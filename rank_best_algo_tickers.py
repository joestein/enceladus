import requests
import bs4 as bs
from signals.macd import get_historical_data, get_macd, implement_macd_strategy
from termcolor import colored as cl
from math import floor
import pandas as pd
import numpy as np

class Ticker():
    def __init__(self, symbol, profit):
        self.symbol = symbol
        self.profit = profit

top_tickers = []
for i in range(20):
    ticker = Ticker(symbol="NA", profit=0)
    top_tickers.append(ticker)

def get_tickers():
    resp = requests.get('http://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    soup = bs.BeautifulSoup(resp.text, 'lxml')
    table = soup.find('table', {'class': 'wikitable sortable'})

    tickers = []

    for row in table.findAll('tr')[1:]:
        ticker = row.findAll('td')[0].text
        tickers.append(ticker)

    print(tickers)

    tickers = [s.replace('\n', '') for s in tickers]

    return tickers

tickers = get_tickers()

for symbol in tickers:

    if symbol in ["BRK.B", "BF.B"]: #doesn't download
        continue 

    ticker = get_historical_data(symbol, '2020-01-01')

    ticker_macd = get_macd(ticker['Close'], 26, 12, 9)
    buy_price, sell_price, macd_signal = implement_macd_strategy(ticker['Close'], ticker_macd)

    position = []
    for i in range(len(macd_signal)):
        if macd_signal[i] > 1:
            position.append(0)
        else:
            position.append(1)
            
    for i in range(len(ticker['Close'])):
        if macd_signal[i] == 1:
            position[i] = 1
        elif macd_signal[i] == -1:
            position[i] = 0
        else:
            position[i] = position[i-1]
            
    macd = ticker_macd['macd']
    signal = ticker_macd['signal']
    close_price = ticker['Close']
    macd_signal = pd.DataFrame(macd_signal).rename(columns = {0:'macd_signal'}).set_index(ticker.index)
    position = pd.DataFrame(position).rename(columns = {0:'macd_position'}).set_index(ticker.index)
    position['position_change'] = position['macd_position'].eq(position['macd_position'].shift())
    print(position.tail(5))

    frames = [close_price, macd, signal, macd_signal, position]
    strategy = pd.concat(frames, join = 'inner', axis = 1)

    ticker_ret = pd.DataFrame(np.diff(ticker['Close'])).rename(columns = {0:'returns'})
    macd_strategy_ret = []

    for i in range(len(ticker_ret)):
        try:
            returns = ticker_ret['returns'][i]*strategy['macd_position'][i]
            macd_strategy_ret.append(returns)
        except:
            pass
        
    macd_strategy_ret_df = pd.DataFrame(macd_strategy_ret).rename(columns = {0:'macd_returns'})

    investment_value = 10000
    number_of_stocks = floor(investment_value/ticker['Close'][0])
    macd_investment_ret = []

    for i in range(len(macd_strategy_ret_df['macd_returns'])):
        returns = number_of_stocks*macd_strategy_ret_df['macd_returns'][i]
        macd_investment_ret.append(returns)

    macd_investment_ret_df = pd.DataFrame(macd_investment_ret).rename(columns = {0:'investment_returns'})
    total_investment_ret = round(sum(macd_investment_ret_df['investment_returns']), 2)
    profit_percentage = floor((total_investment_ret/investment_value)*100)
    print(cl('Profit gained from the MACD strategy by investing $100k in ticker : {}'.format(total_investment_ret), attrs = ['bold']))
    print(cl('Profit percentage of the MACD strategy : {}%'.format(profit_percentage), attrs = ['bold']))

    def get_benchmark(start_date, investment_value):
        spy = get_historical_data('SPY', start_date)['Close']
        benchmark = pd.DataFrame(np.diff(spy)).rename(columns = {0:'benchmark_returns'})
        
        investment_value = investment_value
        number_of_stocks = floor(investment_value/spy[0])
        benchmark_investment_ret = []
        
        for i in range(len(benchmark['benchmark_returns'])):
            returns = number_of_stocks*benchmark['benchmark_returns'][i]
            benchmark_investment_ret.append(returns)

        benchmark_investment_ret_df = pd.DataFrame(benchmark_investment_ret).rename(columns = {0:'investment_returns'})
        return benchmark_investment_ret_df

    benchmark = get_benchmark('2020-01-01', 100000)

    investment_value = 100000
    total_benchmark_investment_ret = round(sum(benchmark['investment_returns']), 2)
    benchmark_profit_percentage = floor((total_benchmark_investment_ret/investment_value)*100)
    print(cl('Benchmark profit by investing $100k : {}'.format(total_benchmark_investment_ret), attrs = ['bold']))
    print(cl('Benchmark Profit percentage : {}%'.format(benchmark_profit_percentage), attrs = ['bold']))
    print(cl('MACD Strategy profit is {}% higher than the Benchmark Profit'.format(profit_percentage - benchmark_profit_percentage), attrs = ['bold']))

    i = 0
    found = False
    for ticker in top_tickers:
        if ticker.profit < profit_percentage and not found:
            top_tickers[i] = Ticker(symbol=symbol, profit=profit_percentage)
            found = True
        
        i += 1

for ticker in top_tickers:
    print(f"Symbol: {ticker.symbol} Profit Percentage: {ticker.profit}")