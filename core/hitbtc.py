'''
API Documentation:
 * Public API v1 (https://hitbtc.com/api#marketrestful)
 * Trade API v2 (https://github.com/hitbtc-com/hitbtc-api/blob/master/APIv2.md)
'''
import json
import requests
import datetime
import hashlib
import hmac
import random
import string
import time
import http.client
import urllib.parse
import urllib.request


# class public api from hitBtc
class public_api(object):
    def __init__(self):
        self.url = 'https://api.hitbtc.com'
        self.conn = http.client.HTTPSConnection('api.hitbtc.com')

    # function to return serv time
    def time(self):
        url = self.url + "/api/2/public/time"
        print(url)
        # print(response.content)
        return requests.get(url).json()

    def symbols(self):
        response = requests.get(self.url + "/api/2/public/symbols")
        print(response.content)
        return response.json()

    # function to return ticker information
    # @pair = Trading symbol (e.g. ETHUSD)
    def ticker(self, tpair):
        url = self.url + "/api/2/public/ticker/" + tpair
        #print(response.content)
        return requests.get(url).json()

    # function to return orderbook
    # @pair = Trading symbol (e.g. ETHUSD)
    def orderbook(self, tpair):
        response = requests.get(self.url + "/api/2/public/" + tpair + "/orderbook")
        #print(response.content)
        return response.json()

    # function to get lasts trades
    # @pair = Trading symbol (e.g. ETHUSD)
    def trades(self, tpair):
        response = requests.get(self.url + "/api/2/public/" + tpair + "/trades")
        #print(response.content)
        return response.json()

    '''
    limit	Number	Limit of candles, default 100.
    period	String	One of: M1 (one minute), M3, M5, M15, M30, H1, H4, D1, D7, 1M (one month). Default is M30 (30 minutes).
    '''


    # class trade api from hi    /api/2/public/candles/{symbol}
    def candles(self, tpair, params):
        url = self.url + "/api/2/public/candles/" + tpair
        # print(response)
        return requests.get(url, params).json()


# class trade api from hitBtc
class trade_api:
    def __init__(self, apiKey, apiSecret):
        self.key = apiKey
        self.secret = apiSecret
        self.nonce = self.rand()
        self.url = "https://api.hitbtc.com"

    # function to create a unique value
    def rand(self):
        return str(int(time.mktime(datetime.datetime.now().timetuple()) * 1000 + datetime.datetime.now().microsecond / 1000))

    #function return balance from all coins
    def balance(self):
        response = requests.get(self.url+'/api/2/trading/balance', auth=(self.key, self.secret))
        #print(r.json())
        return response.json()

    #function to set new order
    #@pair = Trading symbol
    #@transaction = tipe of transaction (sell or buy)
    #@price = trade price
    #@quantity = trade quantity
    def new_order(self,tpair,transaction, quantity, price):
        orderData = {'symbol': tpair, 'side': transaction.lower(), 'quantity': quantity, 'price': price }
        response = requests.post(self.url+'/api/2/order', data = orderData, auth=(self.key, self.secret))
        #print(r.json())
        return response.json()

    #function to cancel orders
    #@pair = Trading symbol
    def cancel_orders(self, tpair=None):
        orderData = {'symbol': tpair}
        response = requests.delete(self.url+'/api/2/order', data = orderData, auth=(self.key, self.secret))
        #print(r.json())
        return response.json()