import sys
sys.path.append('../')

import time
import logging
from OKEX_Account4_SPOT_MA_0905.trade import okex_spot_ma as coin


def print_time():
    try:
        format = '%Y-%m-%d %X'
        time1 = time.strftime(format)

        return time1
    except:
        print ( 'cannot get time !!!!!!!!!!')
        return

if __name__ == '__main__':

    x = 0
    # the parameters in trade list are [m, n, a, b, turtle_threshold, proportion]

    trade_list={
                'btc': ['usdt', 28, 120, 0, 7062, '15min', 0],
                # 'trx': ['usdt', 28, 120, 0, 0,'15min', 3000],
                # 'eth': ['usdt', 28, 120, 0, 0, '15min', 3000],
                'eos': ['usdt', 28, 120, 0, 6.66,'15min', 0],
                'ont': ['usdt', 28, 120, 0, 0,'15min', 0],
                'ada': ['usdt', 28, 120, 0, 0,'15min', 0],
                # 'iost': ['usdt', 28, 120, 0, 0,'15min', 1000],
                }

    while True:
        x += 1
        print('-' * 100)
        print (x, print_time())
        for trade_list_i in trade_list:
            print(trade_list_i,trade_list[trade_list_i])
        print()

        asset_all=0
        for currency in trade_list:
            coin.trade_average_pro(coin1=currency,
                                   coin2=trade_list[currency][0],
                                   m=trade_list[currency][1],
                                   n=trade_list[currency][2],
                                   manual=trade_list[currency][3],
                                   constant=trade_list[currency][4],
                                   interval=trade_list[currency][5],
                                   max_position=trade_list[currency][6])
            asset_all+=coin.total_asset

        asset_all+=coin.coin2_available

        print(trade_list[currency][0],'_available=',round(coin.coin2_available,4),'asset_all=',round(asset_all,4))

        time.sleep(10)



