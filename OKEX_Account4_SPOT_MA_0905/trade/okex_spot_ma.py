import json
import http.client
import ssl
import urllib
import urllib.request
import numpy as np
import time
import os
import logging
from OKEX_Account4_SPOT_MA_0905.okex_api.OkcoinSpotAPI import okex_spot

startup_switch = {
    'btc':0,
    'bch':0,
    'eth':0,
    'neo':0,
    'act':0,
    'iost':0,
    'eos':0,
    'qtum':0,
    'trx':0,
    'etc':0,
    'cmt':0,
    'ont':0,
    'mdt':0,
    'elf':0,
    'snt':0,
    'ada':0,
}
#
# startup_switch = {'neo':0,'eth':0,'eos':0,'bch':0,'trx':0,'etc':0}

def httpGet(resource):
    ssl._create_default_https_context = ssl._create_unverified_context
    url = 'www.okex.com'
    conn = http.client.HTTPSConnection(url, timeout=2)
    conn.request("GET",resource)
    response = conn.getresponse()
    data = response.read().decode('utf-8')
    return json.loads(data)

def get_data(coin1,coin2,m,n,manual,constant,interval):
    global coin_price,coin_buy_price,coin_sell_price
    global coin_average_long,coin_average_short
    global short_long_rate, price_long_rate

    url_current = 'https://www.okex.com/api/v1/ticker.do?symbol='+coin1+'_'+coin2
    data_current = httpGet(url_current)  # convert string to list
    coin_price = float(data_current['ticker']['last'])

    coin_buy_price = coin_price * 1.003
    coin_sell_price = coin_price * 0.997

    url_kline = 'https://www.okex.com/api/v1/kline.do?symbol='+coin1+'_'+coin2+'&type='+interval
    data = httpGet(url_kline)
    data = np.array(data)  # convert list to array
    data = data.astype(np.float)
    data[:, 0] = data[:, 0] / 10000000
    data = data.astype(np.float)
    coin_kline=data[:,1]

    coin_average_short = sum(coin_kline[-m:]) / len(coin_kline[-m:])
    if manual == 1:
        coin_average_long = constant
        manual_ref = sum(coin_kline[-n:]) / len(coin_kline[-n:])
        print('manual_ref =', round(manual_ref, 4))
    else:
        coin_average_long = sum(coin_kline[-n:]) / len(coin_kline[-n:])

    short_long_rate=(coin_average_short/coin_average_long-1)*100
    price_long_rate=(coin_price/coin_average_long-1)*100

def get_asset(coin1,coin2):
        global total_asset, coin1_available, coin2_available

        true = True
        false = False

        max_try_num = 20
        for tries in range(max_try_num):
            try:
                account_info = eval(okex_spot.userinfo())
                break
            except:
                if tries < (max_try_num - 1):
                    continue
                else:
                    logging.error("Has tried %d times to access url, all failed!", max_try_num)
                    break

        coin1_available = float(account_info['info']['funds']['free'][coin1])
        coin2_available = float(account_info['info']['funds']['free'][coin2])

        total_asset = coin_price * coin1_available

def buy(coin1,coin2):
    print('BUY ' + coin1, round(buy_amount * coin_price, 5), coin2)
    true=True
    false=False
    max_try_num = 20
    for tries in range(max_try_num):
        try:
            buy_id=okex_spot.trade(coin1 + '_' + coin2, 'buy', price=coin_buy_price, amount=buy_amount)
            buy_id = eval(buy_id)
            print(buy_id)
            break
        except:
            if tries < (max_try_num - 1):
                continue
            else:
                logging.error('buy failed !')
                return
    if buy_id['result'] == True:
        time.sleep(10)
        try:
            okex_spot.cancelOrder(coin1+'_'+coin2, str(buy_id['order_id']))
        except:
            logging.error('failed to cancel buy order !')

def sell(coin1,coin2):
    print('SELL ' + coin1, round(coin1_value, 5), coin2)
    true=True
    false=False
    max_try_num = 20
    for tries in range(max_try_num):
        try:
            sell_id=okex_spot.trade(coin1 + '_' + coin2, 'sell', price=coin_sell_price, amount=coin1_available)
            sell_id = eval(sell_id)
            print(sell_id)
            break
        except:
            if tries < (max_try_num - 1):
                continue
            else:
                logging.error('sell failed !')
                return
    if sell_id['result'] == True:
        time.sleep(10)
        try:
            okex_spot.cancelOrder(coin1+'_'+coin2, str(sell_id['order_id']))
        except:
            logging.error('failed to cancel sell order !')


def trade_average_pro(coin1, coin2, m, n,manual, constant ,interval,max_position):
    try:
        global buy_amount, coin1_value

        try:
            get_data(coin1=coin1,coin2=coin2,m=m,n=n,manual=manual,constant=constant,interval=interval)
            get_asset(coin1=coin1,coin2=coin2)
        except:
            logging.error('cannot get '+coin1+'_'+coin2+' data')
            return


        if coin_average_short <= coin_average_long:
            startup_switch[coin1] = 1

        print( coin1+'_startup_switch=', startup_switch[coin1])

        print( coin1+'_price =',round(coin_price,4),
               coin1 +'_average_short =',round(coin_average_short,4),
               coin1 +'_average_long =', round(coin_average_long,4))
        print('price_long_rate=', round(price_long_rate, 2), '%',
              'short_long_rate=', round(short_long_rate, 2), '%',)

        coin1_value= float(coin1_available) * coin_price

        buy_amount = max_position / coin_price - coin1_available

        if (coin2_available / coin_price) < buy_amount:
            buy_amount = (coin2_available / coin_price) * 0.99

        if (coin1 == 'btc' or
                coin1 == 'eth' or
                coin1 == 'bch'):
            min_trade_amount = 0.01
        elif coin1 == 'mdt':
            min_trade_amount = 10
        else:
            min_trade_amount = 1

        if buy_amount < min_trade_amount and coin_average_short > coin_average_long:
            print('MET THE PURCHASE LIMIT')
            startup_switch[coin1] = 0

        # Main trading code
        if (coin_average_short > coin_average_long) \
                and buy_amount > min_trade_amount and startup_switch[coin1] == 1:
            buy(coin1,coin2)

        elif (coin_average_short <= coin_average_long) and coin1_available>min_trade_amount:
            startup_switch[coin1] = 1
            sell(coin1,coin2)

        print(coin1 + '_value=', round(coin1_value,4))

        print()

    except:
        logging.error('something wrong in '+coin1+'_'+coin2+' trade_average_pro()')
        return


if __name__=="__main__":
    print()
    # get_data('ltc', 'btc', '15min', 28, 120)
    # get_asset(coin1='ltc',coin2='btc')
# get_data('btc',28,120,5,28)
# trade_average_pro('btc', 28, 120, 5,28,1.1, 1)
