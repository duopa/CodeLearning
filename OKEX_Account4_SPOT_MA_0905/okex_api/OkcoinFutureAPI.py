#!/usr/bin/python
# -*- coding: utf-8 -*-
#用于访问OKCOIN 期货REST API
import json
from OKEX_Account4_SPOT_MA_0905.okex_api.HttpMD5Util import buildMySign,httpGet,httpPost



class OKCoinFuture:

    def __init__(self):
        self.__url = 'www.okex.com'
        self.exchange = "okex"
        self.account = "Account4"

        file_path = 'C:\(Server)\Controller\keyfile.json'
        with open(file_path, 'r') as load_f:
            load_dict = json.load(load_f)
            self.__apikey = load_dict[self.exchange][self.account]['apikey']
            self.__secretkey = load_dict[self.exchange][self.account]['secretkey']

        print(self.account)

    #OKCOIN期货行情信息
    def future_ticker(self,symbol,contractType):
        FUTURE_TICKER_RESOURCE = "/api/v1/future_ticker.do"
        params = ''
        if symbol:
            params += '&symbol=' + symbol if params else 'symbol=' +symbol
        if contractType:
            params += '&contract_type=' + contractType if params else 'contract_type=' +symbol
        return httpGet(self.__url,FUTURE_TICKER_RESOURCE,params)

    #OKCoin期货市场深度信息
    def future_depth(self,symbol,contractType,size): 
        FUTURE_DEPTH_RESOURCE = "/api/v1/future_depth.do"
        params = ''
        if symbol:
            params += '&symbol=' + symbol if params else 'symbol=' +symbol
        if contractType:
            params += '&contract_type=' + contractType if params else 'contract_type=' +symbol
        if size:
            params += '&size=' + size if params else 'size=' + size
        return httpGet(self.__url,FUTURE_DEPTH_RESOURCE,params)

    #OKCoin期货交易记录信息
    def future_trades(self,symbol,contractType):
        FUTURE_TRADES_RESOURCE = "/api/v1/future_trades.do"
        params = ''
        if symbol:
            params += '&symbol=' + symbol if params else 'symbol=' +symbol
        if contractType:
            params += '&contract_type=' + contractType if params else 'contract_type=' +symbol
        return httpGet(self.__url,FUTURE_TRADES_RESOURCE,params)

    #OKCoin期货指数
    def future_index(self,symbol):
        FUTURE_INDEX = "/api/v1/future_index.do"
        params=''
        if symbol:
            params = 'symbol=' +symbol
        return httpGet(self.__url,FUTURE_INDEX,params)

    #获取美元人民币汇率
    def exchange_rate(self):
        EXCHANGE_RATE = "/api/v1/exchange_rate.do"
        return httpGet(self.__url,EXCHANGE_RATE,'')

    #获取预估交割价
    def future_estimated_price(self,symbol):
        FUTURE_ESTIMATED_PRICE = "/api/v1/future_estimated_price.do"
        params=''
        if symbol:
            params = 'symbol=' +symbol
        return httpGet(self.__url,FUTURE_ESTIMATED_PRICE,params)

    #期货全仓账户信息
    def future_userinfo(self):
        FUTURE_USERINFO = "/api/v1/future_userinfo.do?"
        params ={}
        params['api_key'] = self.__apikey
        params['sign'] = buildMySign(params,self.__secretkey)
        return httpPost(self.__url,FUTURE_USERINFO,params)

    #期货全仓持仓信息
    def future_position(self,symbol,contractType):
        FUTURE_POSITION = "/api/v1/future_position.do?"
        params = {
            'api_key':self.__apikey,
            'symbol':symbol,
            'contract_type':contractType
        }
        params['sign'] = buildMySign(params,self.__secretkey)
        return httpPost(self.__url,FUTURE_POSITION,params)

    #期货下单
    def future_trade(self,symbol,contractType,price='',amount='',tradeType='',matchPrice='',leverRate=''):
        FUTURE_TRADE = "/api/v1/future_trade.do?"
        params = {
            'api_key':self.__apikey,
            'symbol':symbol,
            'contract_type':contractType,
            'amount':amount,
            'type':tradeType,
            'match_price':matchPrice,
            'lever_rate':leverRate
        }
        if price:
            params['price'] = price
        params['sign'] = buildMySign(params,self.__secretkey)
        return httpPost(self.__url,FUTURE_TRADE,params)

    #期货批量下单
    def future_batchTrade(self,symbol,contractType,orders_data,leverRate):
        FUTURE_BATCH_TRADE = "/api/v1/future_batch_trade.do?"
        params = {
            'api_key':self.__apikey,
            'symbol':symbol,
            'contract_type':contractType,
            'orders_data':orders_data,
            'lever_rate':leverRate
        }
        params['sign'] = buildMySign(params,self.__secretkey)
        return httpPost(self.__url,FUTURE_BATCH_TRADE,params)

    #期货取消订单
    def future_cancel(self,symbol,contractType,orderId):
        FUTURE_CANCEL = "/api/v1/future_cancel.do?"
        params = {
            'api_key':self.__apikey,
            'symbol':symbol,
            'contract_type':contractType,
            'order_id':orderId
        }
        params['sign'] = buildMySign(params,self.__secretkey)
        return httpPost(self.__url,FUTURE_CANCEL,params)

    #期货获取订单信息
    def future_orderinfo(self,symbol,contractType,orderId,status,currentPage,pageLength):
        FUTURE_ORDERINFO = "/api/v1/future_order_info.do?"
        params = {
            'api_key':self.__apikey,
            'symbol':symbol,
            'contract_type':contractType,
            'order_id':orderId,
            'status':status,
            'current_page':currentPage,
            'page_length':pageLength
        }
        params['sign'] = buildMySign(params,self.__secretkey)
        return httpPost(self.__url,FUTURE_ORDERINFO,params)

    #期货逐仓账户信息
    def future_userinfo_4fix(self):
        FUTURE_INFO_4FIX = "/api/v1/future_userinfo_4fix.do?"
        params = {'api_key':self.__apikey}
        params['sign'] = buildMySign(params,self.__secretkey)
        return httpPost(self.__url,FUTURE_INFO_4FIX,params)

    #期货逐仓持仓信息
    def future_position_4fix(self,symbol,contractType,type1):
        FUTURE_POSITION_4FIX = "/api/v1/future_position_4fix.do?"
        params = {
            'api_key':self.__apikey,
            'symbol':symbol,
            'contract_type':contractType,
            'type':type1
        }
        params['sign'] = buildMySign(params,self.__secretkey)
        return httpPost(self.__url,FUTURE_POSITION_4FIX,params)




    # def cancel_future_orders(self, coin):
    #     # try:
    #         orders = self.future_trades(coin+'_usd', 'quarter')
    #         print(orders)
    #         # true = True
    #         # orders = orders['tid']
    #         #
    #         # ids = []
    #         # for n in orders:
    #         #     ids.append(n['order_id'])
    #         #
    #         # if ids == None:
    #         #     print('okcoin has nothing to clear')
    #         #     return
    #         #
    #         # for id in ids:
    #         #     self.cancelOrder(self, coin+'_cny', id)
    #         # print('ok coin orders clear')
    #
    #     # except:
    #     #     print('failed to cancel okcoin orders')
    #     #     return


okex_future=OKCoinFuture()


if __name__ == '__main__':


    # okex_future.cancel_future_orders('btc')
    # buy_long_id = okex_future.future_trade('btc_usd', 'quarter', '1', '0.001', '1', '0','10')
    # print(buy_long_id)

    print(u'期货下单')
    print(okex_future.future_trade('btc_usd', 'this_week', '0.1','1', '4', '1', '10'))




    
