#bitfinex setup
#Taylor Webber

from urllib2 import urlopen
import json

url = 'https://api.bitfinex.com/v1'
pair_url = url + '/symbols'
ticker_url = url + '/pubticker/'

#update available pairs for trade from Bitfinex
def update_pairs():
    response = urlopen(pair_url)
    json_obj = json.load(response)
    bitfinex_pair_library = [[]] * 6

    # Uncomment to view JSON output from API   
    #f = open('output_bitfinex.json', 'w')
    #f.write(json.dumps(json_obj, indent=4))
    #f.close()

    count = 0

    for pair in json_obj:
        bitfinex_pair_library[count] = pair
        count += 1
    
    return bitfinex_pair_library

class BitfinexTicker:
    def __init__(self, pair):        
        self.set_pair(pair)
        
        url_ticker = ticker_url + self.pair
        response = urlopen(url_ticker)
        json_obj = json.load(response)
        
        # Uncomment to view JSON output from API   
        #f = open('output_bitfinex_ticker.json', 'w')
        #f.write(json.dumps(json_obj, indent=4))
        #f.close()

        self.mid = json_obj['mid']
        self.bid = json_obj['bid']
        self.ask = json_obj['ask']
        self.last = json_obj['last_price']
        self.low = json_obj['low']
        self.high = json_obj['high']
        self.volume = json_obj['volume']
    
    @classmethod
    #set pair for Ticker
    def set_pair(self, pair):
        self.pair = pair
        
    def update_ticker(self):
        url_ticker = ticker_url + self.pair
        response = urlopen(url_ticker)
        json_obj = json.load(response)
        
        self.mid = json_obj['mid']
        self.bid = json_obj['bid']
        self.ask = json_obj['ask']
        self.last = json_obj['last_price']
        self.low = json_obj['low']
        self.high = json_obj['high']
        self.volume = json_obj['volume']


