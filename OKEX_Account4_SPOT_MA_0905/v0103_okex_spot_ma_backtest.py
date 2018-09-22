# -*- coding: utf-8 -*-
"""
Created on Thu May  4 00:04:01 2017

@author: lenovo
"""
import urllib
import numpy as np
import matplotlib.pyplot as plt
import time
import os


def get_data(coin, interval):
    global data

    # url_current = 'https://www.okex.com/api/v1/ticker.do?symbol='+coin
    # webpage_current = urllib.request.urlopen(url_current)  # open url
    # content_current = webpage_current.read()  # read webpage content
    # data_current = eval(content_current)  # convert string to list
    # print ( 'data_current=', data_current)
    # price_current = data_current['ticker']['last']
    # print ( 'price_current=',price_current)

    url_001 = 'https://www.okex.com/api/v1/kline.do?symbol='+coin+'&type='+interval
    webpage = urllib.request.urlopen(url_001,timeout=2)
    content = webpage.read()
    data = eval(content)
    data = np.array(data)  # convert list to array
    data = data.astype(np.float)
    data[:, 0] = data[:, 0] / 10000000
    data = data.astype(np.float)
    kline=data[:,1]

    print(kline)

def buy(backtest_length, ma_long):
    global wealth, cny, coin_price, ltc_amount,i

    print ( 'BUY ltc')
    wealth = wealth * 0.5
    quantity_buy = cny / coin_price
    ltc_amount = quantity_buy + ltc_amount
    cny = cny - quantity_buy * coin_price
    ltc_amount = ltc_amount * 0.997

    print ( 'cny=', cny)
    print ( 'ltc=', ltc_amount)
    print ( 'wealth=', wealth)
    plt.plot(i + backtest_length - ma_long, coin_price, 'or')
    plt.text(i + backtest_length - ma_long, coin_price, '%s' % (coin_price))

def sell(backtest_length, ma_long):
    global wealth, cny, coin_price, ltc_amount,i

    print ( 'SELL ltc')
    wealth = wealth * 0.5
    quantity_sell = ltc_amount
    cny = quantity_sell * coin_price + cny
    ltc_amount = ltc_amount - quantity_sell
    cny = cny * 0.997

    print ( 'cny=', cny)
    print ( 'ltc=', ltc_amount)
    print ( 'wealth=', wealth)
    plt.plot(i + backtest_length - ma_long, coin_price, 'ob')
    plt.text(i + backtest_length - ma_long, coin_price, '%s' % (coin_price))

def trade(ma_short, ma_long, ma2_short, ma2_long,
          backtest_length, turtle_thredhold, interval, coin):
    global wealth,cny, coin_price, ltc_amount,i

    get_data(coin, interval)

    i = -(backtest_length - ma_long)
    i1 = i
    j = i - ma_short  # the number means the average of the number of minutes
    k = i - ma_long
    a = i - ma2_short
    b = i - ma2_long
    l = i - 10

    cny = 100000
    cny1 = cny
    ltc_amount = 0

    startup_switch=0
    turtle_switch=0


    figure_001 = []
    figure_average_short = []
    figure_average_long = []
    figure_average2_short = []
    figure_average2_long = []

    volume = []
    figure_volume_average = []

    figure_wealth = []



    plt.figure()
    plt.subplot(311)

    while i < 0:


        coin_price = data[i, 1]
        data_average_short = sum(data[j:i, 1]) / len(data[j:i, 1])  # get average
        data_average_long = sum(data[k:i, 1]) / len(data[k:i, 1])

        data_average2_short = sum(data[a:i, 1]) / len(data[a:i, 1])
        data_average2_long = sum(data[b:i, 1]) / len(data[b:i, 1])


        if data_average_short <= data_average_long:
            startup_switch = 1
            turtle_switch=0

        if data_average2_short > data_average_long * turtle_thredhold \
                and data_average_short>data_average_long:
            turtle_switch = 1

        data_volume_average = sum(data[l:i, 5]) / len(data[l:i, 5])

        print ( i, 'current_price=', coin_price, 'data_average_short=', data_average_short, 'data_average_long=',data_average_long)
        print ( 'startup_switch=', startup_switch, 'turtle_switch=', turtle_switch)

        figure_001.append(data[i, 1])
        figure_average_short.append(data_average_short)
        figure_average_long.append(data_average_long)
        figure_average2_short.append(data_average2_short)
        figure_average2_long.append(data_average2_long)

        volume.append(data[i, 5])
        figure_volume_average.append(data_volume_average)

        coin_price = data[i, 1]

        wealth = cny + ltc_amount * coin_price
        if data_average_long * turtle_thredhold >= data_average_short > data_average_long and ltc_amount == 0 and turtle_switch == 0 and startup_switch == 1:
            buy(backtest_length, ma_long)

        elif data_average2_short > data_average2_long and turtle_switch == 1 and ltc_amount == 0 and startup_switch == 1:
                buy(backtest_length, ma_long)

        elif data_average2_short <= data_average2_long and turtle_switch == 1 and ltc_amount != 0:
                startup_switch = 1
                sell(backtest_length, ma_long)


        elif data_average_short <= data_average_long and ltc_amount != 0:
            startup_switch=1
            turtle_switch=0

            sell(backtest_length, ma_long)


        coin_price = data[i, 1]
        wealth = cny + ltc_amount * coin_price

        figure_wealth.append(wealth)

        i += 1
        j += 1
        k += 1
        l += 1
        a += 1
        b += 1

    print ( 'cny=', str(cny))
    print ( 'ltc=', ltc_amount)
    print ( 'wealth=', wealth)
    print ( 'profit=', (wealth - cny1) / cny1 * 100, '%')
    print ( 'standard profit=', (data[-1, 1] - data[i1, 1]) / data[i1, 1] * 100, '%')


    plt.plot(figure_001,'yellow')
    plt.plot(figure_average_short,'dimgray')
    plt.plot(figure_average_long,'black')
    plt.plot(figure_average2_short,'lightgreen')
    plt.plot(figure_average2_long,'green')

    plt.subplot(312)
    plt.plot(volume, 'g')
    plt.plot(figure_volume_average, 'r')

    plt.subplot(313)
    plt.plot(figure_wealth)

    plt.show()

trade(ma_short=7,
      ma_long=30,
      ma2_short=7,
      ma2_long=30,
      backtest_length=530,
      turtle_thredhold=1.5,
      interval='1hour',
      coin='eth_btc')


# if __name__=='__main__':
#
#     get_data('btc_usdt','15min')

