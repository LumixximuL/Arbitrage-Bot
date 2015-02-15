#Market Watcher
#Taylor Webber

import market
import btcetrade
import bitfinextrade
import configure
import time

#Market Watcher object creates traders and market
class MarketWatcher:
    def __init__(self):
        print "Creating BTC-e trader"
        self.btce_trader = btcetrade.BTCeTrader(configure.btc_e_key, configure.btc_e_secret)
        #self.bitstamp_trader = bitstampsetup.BitStampTicker()
        print "Creating Bitfinex trader"
        self.bitfinex_trader = bitfinextrade.BitfinexTrader(configure.bitfinex_key, configure.bitfinex_secret)
        print "Creating market for btc-usd"
        self.current_market = market.Market()
    
    #loops until viable trade is found    
    def auto_trade(self, searches):
        self.current_market.start_market()
        self.buy, self.buy_exchange = self.current_market.get_min_buy()
        self.sell, self.sell_exchange = self.current_market.get_max_sell()
        
        max_profit_percent = 0
        max_profit = 0
        count = 0
        buy_fee = 0
        sell_fee = 0
        self.trade = 0
        
        self.buy_total = 0
        self.sell_total = 0
        self.profit = 0
        self.profit_percent = 0
        
        while count < searches:
            #get fees
            if self.buy_exchange == 'BTC-e':
                buy_fee = configure.btc_e_fee
            elif self.buy_exchange == 'Bitfinex':
                buy_fee = configure.bitfinex_fee
            else:
                print "Error: Buy exchange fee not found"
            
            if self.sell_exchange == 'BTC-e':
                sell_fee = configure.btc_e_fee
            elif self.sell_exchange == 'Bitfinex':
                sell_fee = configure.bitfinex_fee
            else:
                print "Error: Sell exchange fee not found"
            
            #calculate the amount purchased with fees included
            self.buy_total = float(self.buy) * configure.volume * (1 + buy_fee)
            self.sell_total = float(self.sell) * configure.volume * (1 - sell_fee)
            
            #profit and profit percent with fees included
            self.profit = self.sell_total - self.buy_total
            self.profit_percent = (1 - (self.buy_total / self.sell_total)) * 100
            
            if self.profit_percent > configure.cutoff:
                #chance for profit
                max_profit_percent = self.profit_percent
                max_profit = self.profit
                self.trade = 1
                break;
            elif self.profit_percent < configure.buy_back:
                #chance to complete arbitrage cycle
                max_profit_percent = self.profit_percent
                max_profit = self.profit
                self.trade = 2
                break;
            else:
                print self.buy_exchange, ": ", self.buy
                print self.sell_exchange, ": ", self.sell
                print self.profit, " dollars"
                print self.profit_percent, " percent"
            
                time.sleep(5)
            
                self.current_market.update_market()
                self.buy, self.buy_exchange = self.current_market.get_min_buy()
                self.sell, self.ell_exchange = self.current_market.get_max_sell()
            
                count += 1
                
        self.execute_transaction()
                
    #execute the transaction if trade was found
    def execute_transaction(self):
        #trade found execute trade
        if self.trade == 1:
        
            #complete buy
            if self.buy_exchange == 'BTC-e':
                            
                print "Buy on BTC-e"
                #call BTC-e buy module
            
                #self.buy_response = self.btce_trader.Trade("btc_usd", "buy", configure.volume, configure.volume)
                #self.buy_trans_key = self.buy_response['return']['order_id]
                
            elif self.buy_exchange == 'BitStamp':
                print "Buy on BitStamp"
                #call BitStamp buy module
            
            elif self.buy_exchange == 'Bitfinex':
                print "Buy on Bitfinex"
                #call Bitfinex buy module
            
                #self.buy_response = self.bitfinex_trader.Trade("btcusd", configure.volume, self.buy, "buy", "market")
                #self.buy_trans_key = self.buy_response['order_id']
                
            else:
                #trade not found
                print "Error: Buy Exchange not found"
                
            #complete sell
            if self.sell_exchange == 'BTC-e':
                print "Sell on BTC-e"
                #call BTC-e sell module
            
                #self.sell_response = self.btce_trader.Trade("btc_usd", "sell", configure.volume, configure.volume)
                #self.sell_trans_key = self.sell_response['return']['order_id']
                
            elif self.sell_exchange == 'BitStamp':
                print "Sell on BitStamp"
                #call BitStamp sell module
                
            elif self.sell_exchange == 'Bitfinex':
                print "Sell on Bitfinex"
                #call Bitfinex sell module
            
                #self.sell_response = self.bitfinex_trader.Trade("btcusd", configure.volume, self.sell, "sell", "market")
                #self.sell_trans_key = self.sell_response['order_id']
                
            else:
                #sell exchange not found
                print "Error: Sell Exchange not found"
            
            self.document_trade()
            
        #complete Arbitrage cycle
        elif self.trade == 2:
            print "Completing Arbitrage cycle"
            #complete sell on buy exchange
            if self.buy_exchange == 'BTC-e':
                print "Sell on BTC-e"
                #call BTC-e buy module
                
                complete_buy = self.get_funds('btc', self.buy_exchange)
                print complete_buy
                
                #self.buy_response = self.btce_trader.Trade("btc_usd", "sell", configure.volume, complete_buy)
                #self.buy_trans_key = self.buy_response['return']['order_id]
                
            elif self.buy_exchange == 'BitStamp':
                print "Sell on BitStamp"
                #call BitStamp buy module
            
            elif self.buy_exchange == 'Bitfinex':
                print "Sell on Bitfinex"
                #call Bitfinex buy module
                
                complete_buy = self.get_funds('btc', self.buy_exchange)
                print complete_buy
            
                #self.buy_response = self.bitfinex_trader.Trade("btcusd", conmplete_buy, self.buy, "buy", "market")
                #self.buy_trans_key = self.buy_response['order_id']
                
            else:
                #trade not found
                print "Error: Buy Exchange not found"
                
        
            #complete buy on sell exchange
            if self.sell_exchange == 'BTC-e':
                print "Buy on BTC-e"
                #call BTC-e sell module
                
                complete_sell = self.get_funds('usd', self.buy_exchange)
                print complete_sell
                
                #self.sell_response = self.btce_trader.Trade("btc_usd", "sell", configure.volume, complete_sell)
                #self.sell_trans_key = self.sell_response['return']['order_id']
                
            elif self.sell_exchange == 'BitStamp':
                print "Buy on BitStamp"
                #call BitStamp sell module
                
            elif self.sell_exchange == 'Bitfinex':
                print "Buy on Bitfinex"
                #call Bitfinex sell module
                
                complete_sell = self.get_funds('usd', self.buy_exchange)
                print complete_sell
                
                #self.sell_response = self.bitfinex_trader.Trade("btcusd", complete_sell, self.sell, "sell", "market")
                #self.sell_trans_key = self.sell_response['order_id']
                
            else:
                #sell exchange not found
                print "Error: Sell Exchange not found"
            
            self.document_trade()
        else:
            print "No trade found"  

    def document_trade(self):
        #Document trade in text file
        output_file = open("testdata.txt", "a")
        output_file.write(time.strftime("%a, %d %b %Y %H:%M:%S    ", time.localtime()))
        output_file.write("{0:10}".format(self.buy_exchange))
        output_file.write("{0:14}".format(str(self.buy_total)))
        output_file.write("{0:10}".format(self.sell_exchange))
        output_file.write("{0:13}".format(str(self.sell_total)))
        output_file.write("{0:17}".format(str(self.profit_percent)))
        output_file.write(str(self.profit))
        output_file.write("\n")
        output_file.close()
        
        print ""
        print ""
        print "Should I make a trade? ", self.trade
        if self.trade == 1:
            print self.buy_exchange, ": ", self.buy
            print self.sell_exchange,": ", self.sell
            print self.profit_percent, " percent"
            print self.profit, " dollars"
    
    #Find total funds to complete arbitrage
    def get_funds(self, currency, exchange):
        funds = 0
        if exchange == 'BTC-e':
            print "Finding funds on BTC-e"
            account = self.btce_trader.getInfo()
            funds = account['return']['funds'][currency]
            print funds
        
        elif exchange == 'Bitstamp':
            #Exchange not currently in use
            funds = 0
        elif exchange == 'Bitfinex':
            print "Finding funds on Bitfinex"
            #NEED TO CODE
            print "bitfinex"
        else:
            #exchange not found
            print "Error: Funds exchange not found"
        
        return funds
            
    def validate_trade(self):
        trade_completed = 0
        times_checked = 0
        buy_checker = 0
        sell_checker = 0
        
        while trade_completed < 1:
            #call to api for completed trade info
            
            if buy_checker < 1:
                #Check the buying market
                if self.buy_exchange == 'BTC-e':
            
                    print "Checking buy transaction on BTC-e"
                    #call BTC-e account module
            
                    #buy_response = self.btce_trader.OrderInfo(self.buy_trans_key)
                    #buy_checker = buy_response['return'][self.buy_trans_key]['status']
                    
                elif self.buy_exchange == 'BitStamp':
                    print "Checking buy transaction on BitStamp"
                    #call BitStamp account module
            
                elif self.buy_exchange == 'Bitfinex':
                    print "Checking buy transaction on Bitfinex"
                    #call Bitfinex account module
            
                    #buy_checker_response = self.bitfinex_trader.OrderStatus(self.buy_trans_key)
                    #remaining = buy_checker_response['remaining_amount']
                    #original = buy_checker_response['original_amount']
                    #if remaining == original:
                        #buy_checker = 1
                    
            if sell_checker < 1:
                #Check the  selling market
                if self.sell_exchange == 'BTC-e':
                    print "Checking sell transaction on BTC-e"
                    #call BTC-e account module
            
                    #sell_response = self.btce_trader.OrderInfo(self.sell_trans_key)
                    #sell_checker = sell_response['return'][self.sell_trans_key]['status']
                    
                elif self.sell_exchange == 'BitStamp':
                    print "Checking sell transaction on BitStamp"
                    #call BitStamp account module
                
                elif self.sell_exchange == 'Bitfinex':
                    print "Checking sell transaction on Bitfinex"
                    #call Bitfinex account module
            
                    #sell_checker_response = self.bitfinex_trader.OrderStatus(self.sell_trans_key)       
                    #remaining = sell_checker_response['remaining_amount']
                    #original = sell_checker_response['original_amount']
                    #if remaining == original:
                        #sell_checker = 1
            
            if buy_checker >= 1:
                if sell_checker >= 1:
                    trade_completed = 1
            if times_checked > 2:
                break;
            times_checked += 1
            #make sleep time 30 when done testing
            time.sleep(10)
            
        return trade_completed
        