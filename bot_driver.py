#Loops each time a trade is completed for Arbitrage
#Taylor Webber

import market_watcher
import btcetrade
import bitfinextrade
import configure
import time

#main function stub
def main():
    
    #trades_completed holds the number of succcessful trades completed
    trades_completed = 0
    trade_validated = 1
    num_of_searches = 10
    
    while trades_completed < configure.num_of_trades:
        if trade_validated > 0:
            Trader = market_watcher.MarketWatcher()
            Trader.auto_trade(configure.num_of_searches)
            trade_validated = 0
        
        #The next line will be deleted once application goes live
        trades_completed = 1
        
        
        #Uncomment these lines of code once app goes live        
        #transaction_done = Trader.validate_trade()
        #if transaction_done > 0:
            #trades_completed += 1
            #trade_validated = 1
        
    
# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()