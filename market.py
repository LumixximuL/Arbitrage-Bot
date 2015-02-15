#Market Object
#Taylor Webber

import btcesetup
import bitstampsetup
import bitfinexsetup
import configure
import time

#Market Object
class Market:
    def __init__(self):
        self.btce_ticker = btcesetup.BTCeTicker('btc_usd')
        #self.bitstamp_ticker = bitstampsetup.BitStampTicker()
        self.bitfinex_ticker = bitfinexsetup.BitfinexTicker('btcusd')
        self.btce_buy = 0
        self.btce_sell = 0
        #self.bitstamp_buy = 0
        #self.bitstamp_sell = 0
        self.bitfinex_buy = 0
        self.bitfinex_sell = 0
    
    def start_market(self):
        self.btce_buy = self.btce_ticker.buy
        self.btce_sell = self.btce_ticker.sell
        #self.bitstamp_buy = self.bitstamp_ticker.bid
        #self.bitstamp_sell = self.bitstamp_ticker.ask
        self.bitfinex_buy = self.bitfinex_ticker.bid
        self.bitfinex_sell = self.bitfinex_ticker.ask
        
    def update_market(self):
        self.btce_ticker.generate_ticker()
        #self.bitstamp_ticker.update_ticker()
        self.bitfinex_ticker.update_ticker()
        
        self.btce_buy = self.btce_ticker.buy
        self.btce_sell = self.btce_ticker.sell
        #self.bitstamp_buy = self.bitstamp_ticker.bid
        #self.bitstamp_sell = self.bitstamp_ticker.ask
        self.bitfinex_buy = self.bitfinex_ticker.bid
        self.bitfinex_sell = self.bitfinex_ticker.ask
        
    def get_min_buy(self):
        min = self.btce_buy
        exchange = 'BTC-e'
        
        #if self.bitstamp_buy < min:
            #min = self.bitstamp_buy
            #exchange = 'BitStamp'
        if self.bitfinex_buy < min:
            min = self.bitfinex_buy
            exchange = 'Bitfinex'
            
        return min, exchange
    
    def get_max_sell(self):
        max = self.btce_sell
        exchange = 'BTC-e'
        
        #if self.bitstamp_buy > max:
            #max = self.bitstamp_sell
            #exchange = 'BitStamp'
        if self.bitfinex_buy > max:
            max = self.bitfinex_sell
            exchange = 'Bitfinex'
            
        return max, exchange
    