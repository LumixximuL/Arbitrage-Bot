#Test the watch structure of the bot

import BTCeTicker
import configure
import bitstampsetup
import bitfinexsetup
import time

#main function stub
def main():
    #update currency pair library to current pairs
    pair_library, fee_library = BTCeTicker.update_pairs()
    
    
    #create BTCeTicker object for BTC-e specify pair
    btc_usd_ticker = BTCeTicker.BTCeTicker('btc_usd')
    #create BitStampTicker object (for btc only)
    bitstamp_ticker = bitstampsetup.BitStampTicker()
    #create BitfinexTicker object
    bitfinex_ticker = bitfinexsetup.BitfinexTicker('btcusd')
    
    btce_price = btc_usd_ticker.buy
    bitstamp_price = bitstamp_ticker.ask
    bitfinex_price = bitfinex_ticker.ask
    
    btce_total = float(btce_price) * configure.volume * (1 + fee_library['btc_usd'])
    bitstamp_total = float(bitstamp_price) * configure.volume * (1 - .005)
    bitfinex_total = float(bitfinex_price) * configure.volume * (1 - .005)
    
    profit_bitstamp = bitstamp_total - btce_total
    profit_bitfinex = bitfinex_total - btce_total
    
    percent_bitstamp = 1 - (btce_total / bitstamp_total)
    checker_bitstamp = percent_bitstamp * 100
    
    percent_bitfinex = 1 - (btce_total / bitfinex_total)
    checker_bitfinex = percent_bitfinex * 100
    
    counter = 0
    max_profit_percent = 0
    trade = 0
    trade_market = ''
    
    while counter < 10:
        if checker_bitstamp > configure.cutoff:
            max_profit_percent = checker_bitstamp
            trade = 1
            trade_market = 'Bitstamp'
            break;
        elif checker_bitfinex > configure.cutoff:
            max_profit_percent = checker_bitfinex
            trade = 1
            trade_market = 'Bitfinex'
            break;
        else:
            if checker_bitstamp > max_profit_percent:
                max_profit_percent = checker_bitstamp
            elif checker_bitfinex > max_profit_percent:
                max_profit_percent = checker_bitfinex
                
        print "BTC-e price: ", btce_price
        print "BitStamp price: ", bitstamp_price
        print "Bitfinex price: ", bitfinex_price
        print max_profit_percent
        
        time.sleep(5)
                
        btc_usd_ticker.generate_ticker()
        bitstamp_ticker.update_ticker()
        bitfinex_ticker.update_ticker()
        
        btce_price = btc_usd_ticker.buy
        bitstamp_price = bitstamp_ticker.ask
        bitfinex_price = bitfinex_ticker.ask
    
        btce_total = float(btce_price) * configure.volume * (1 + fee_library['btc_usd'])
        bitstamp_total = float(bitstamp_price) * configure.volume * (1 - .005)
        bitfinex_total = float(bitfinex_price) * configure.volume * (1 - .005)
    
        profit_bitstamp = bitstamp_total - btce_total
        profit_bitfinex = bitfinex_total - btce_total
    
        percent_bitstamp = 1 - (btce_total / bitstamp_total)
        checker_bitstamp = percent_bitstamp * 100
    
        percent_bitfinex = 1 - (btce_total / bitfinex_total)
        checker_bitfinex = percent_bitfinex * 100
        
        counter += 1
    print ""
    print ""            
    print "Should I make a trade?", trade
    print "BTC-e price: ", btce_price
    print "BitStamp price: ", bitstamp_price
    print "Bitfinex price: ", bitfinex_price
    if trade == 1:
            print "Profit of: ", profit_test, " dollars"
    print max_profit_percent
    

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()