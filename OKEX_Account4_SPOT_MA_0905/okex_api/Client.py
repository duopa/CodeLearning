#!/usr/bin/python
# -*- coding: utf-8 -*-
# encoding: utf-8
#客户端调用，用于查看API返回结果


from OKEX_Account4_SPOT_MA_0905.okex_api.OkcoinFutureAPI import okex_future

if __name__=='__main__':

    #初始化apikey，secretkey,url
    apikey = '7e9273bd-567f-4361-8b90-ba9bbb001b43'
    secretkey = 'A3FADAC6CE1A27FEDA42AFA81739A918'
    okcoinRESTURL = 'www.okcoin.com'   #请求注意：国内账号需要 修改为 www.okcoin.cn

    #期货API
    okcoinFuture = okex_future(okcoinRESTURL,apikey,secretkey)

    # print (u' 期货行情信息')
    # print (okcoinFuture.future_ticker('ltc_usd','this_week'))

    #print (u' 期货市场深度信息')
    #print (okcoinFuture.future_depth('btc_usd','this_week','6'))

    #print (u'期货交易记录信息')
    #print (okcoinFuture.future_trades('ltc_usd','this_week'))

    #print (u'期货指数信息')
    #print (okcoinFuture.future_index('ltc_usd'))

    #print (u'美元人民币汇率')
    #print (okcoinFuture.exchange_rate())

    #print (u'获取预估交割价')
    #print (okcoinFuture.future_estimated_price('ltc_usd'))

    #print (u'获取全仓账户信息')
    #print (okcoinFuture.future_userinfo())

    #print (u'获取全仓持仓信息')
    #print (okcoinFuture.future_position('ltc_usd','this_week'))

    print (u'期货下单')
    print (okcoinFuture.future_trade('ltc_usd','this_week','0.1','1','1','0','20'))

    #print (u'期货批量下单')
    #print (okcoinFuture.future_batchTrade('ltc_usd','this_week','[{price:0.1,amount:1,type:1,match_price:0},{price:0.1,amount:3,type:1,match_price:0}]','20'))

    #print (u'期货取消订单')
    #print (okcoinFuture.future_cancel('ltc_usd','this_week','47231499'))

    #print (u'期货获取订单信息')
    #print (okcoinFuture.future_orderinfo('ltc_usd','this_week','47231812','0','1','2'))

    #print (u'期货逐仓账户信息')
    #print (okcoinFuture.future_userinfo_4fix())

    #print (u'期货逐仓持仓信息')
    #print (okcoinFuture.future_position_4fix('ltc_usd','this_week',1))



   
