#Tester

import btcesetup
import configure
import bitstampsetup
import bitfinexsetup

#main function stub
def main():

    #update currency pair library to current pairs
    pair_library, fee_library = BTCeTicker.update_pairs()
    print pair_library
    print fee_library
    
    #create BTCeTicker object for BTC-e specify pair
    btc_usd_ticker = btcesetup.BTCeTicker('btc_usd')    
    ltc_usd_ticker = btcesetup.BTCeTicker('ltc_usd')
    ltc_btc_ticker = btcesetup.BTCeTicker('ltc_btc')    
    
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
    profit_test_btce_bitstamp = bitstamp_total - btce_total
    profit_test_btce_bitfinex = bitfinex_total - btce_total
    
    profit_percent = 1 - (btce_total / bitstamp_total)
    profit_percent_bitstamp = profit_percent * 100
    
    profit_percent = 1 - (btce_total / bitfinex_total)
    profit_percent_bitfinex = profit_percent * 100
    
    
    print "BTC-e price: ", btce_price
    print "BitStamp price: ", bitstamp_price
    print "Bitfinex price: ", bitfinex_price
    print "If execute trade of 0.1 BTC"
    print "BTC-e/Bitstamp profit of: ", profit_test_btce_bitstamp, " dollars"
    print "which is: ", profit_percent_bitstamp, " percent"
    print "BTC-e/Bitfinex profit of: ", profit_test_btce_bitfinex, " dollars"
    print "which is: ", profit_percent_bitfinex, " percent"
    
# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()