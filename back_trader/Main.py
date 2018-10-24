from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import datetime  # For datetime objects
import os.path  # To manage paths
import sys  # To find out the script name (in argv[0])
import pandas as pd
# from WindPy import w
# Import the backtrader platform
import backtrader as bt
from TestStrategy import TestStrategy
from TestStrategy2 import TestStrategy2
from TestStrategy3 import TestStrategy3
from TestStrategy4 import TestStrategy4

if __name__ == '__main__':
    init_cash = 10000



    # Create a cerebro entity
    cerebro = bt.Cerebro()

    # Add a strategy
    cerebro.addstrategy(TestStrategy4)

    # cerebro.optstrategy(
    #     TestStrategy4,
    #     ma_short=range(1,50),
    #     ma_long=range(30,200)
    #     )

    # Create a Data Feed
    # 本地数据，笔者用Wind获取的东风汽车数据以csv形式存储在本地。
    # parase_dates = True是为了读取csv为dataframe的时候能够自动识别datetime格式的字符串，big作为index
    # 注意，这里最后的pandas要符合backtrader的要求的格式
    dataframe = pd.read_csv('dfqc.csv', index_col=0, parse_dates=True)
    dataframe['openinterest'] = 0
    data = bt.feeds.PandasData(dataname=dataframe,
                                fromdate = datetime.datetime(2013, 1, 1),
                                todate = datetime.datetime(2017, 12, 31),
                                timeframe = bt.TimeFrame.Days
                               )
    # Add the Data Feed to Cerebro
    cerebro.adddata(data)

    # 加入另外一个新的timeframe的datafeed的时候，就不能是adddata了，而是之前说的resampling
    # cerebro.resampledata(data, timeframe=bt.TimeFrame.Weeks)

    # Set our desired cash start
    cerebro.broker.setcash(init_cash)

    # 设置每笔交易交易的股票数量
    cerebro.addsizer(bt.sizers.FixedSize, stake=init_cash * 0.5)
    # Set the commission
    cerebro.broker.setcommission(commission=0.001)

    # Print out the starting conditions
    print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())
    cerebro.addanalyzer(bt.analyzers.SharpeRatio, _name='SharpeRatio')
    cerebro.addanalyzer(bt.analyzers.DrawDown, _name='DW')
    # Run over everything
    results = cerebro.run()
    strat = results[0]
    # Print out the final result
    print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())
    print('SR:', strat.analyzers.SharpeRatio.get_analysis())
    print('DW:', strat.analyzers.DW.get_analysis())
    # Plot the result
    cerebro.plot(style='bar')

