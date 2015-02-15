#Ticker object
#Taylor Webber

import json
from urllib2 import urlopen

btc_e_pair_library = [[]] * 30
btc_e_fee_dict = {}
url = "https://btc-e.com/api/3/info"

#place active pairs in the library from BTC-e
def update_pairs():
    response = urlopen(url)
    json_obj = json.load(response)
    
    
    num_of_pairs = 0
    
    for pair in json_obj['pairs']:
        btc_e_pair_library[num_of_pairs].append(pair)
        btc_e_fee_dict[pair] = json_obj['pairs'][pair]['fee'] / 100
        num_of_pairs += 1
    
    return btc_e_pair_library[0], btc_e_fee_dict


#Creates a Ticker class for a set pair
class BTCeTicker:
    def __init__(self, pair):        
        self.set_pair(pair)
        
        url = "https://btc-e.com/api/3/ticker/" + self.pair
        response = urlopen(url)
        json_obj = json.load(response)

        self.high = json_obj[self.pair]['high']
        self.low = json_obj[self.pair]['low']
        self.avg = json_obj[self.pair]['avg']
        self.vol = json_obj[self.pair]['vol']
        self.vol_cur = json_obj[self.pair]['vol_cur']
        self.last = json_obj[self.pair]['last']
        self.buy = json_obj[self.pair]['buy']
        self.sell = json_obj[self.pair]['sell']
    
    
    @classmethod
    #set pair for Ticker
    def set_pair(self, pair):
        self.pair = pair
    
    @classmethod
    #get ticker info
    def generate_ticker(self):
        url = "https://btc-e.com/api/3/ticker/" + self.pair
        response = urlopen(url)
        json_obj = json.load(response)

        self.high = json_obj[self.pair]['high']
        self.low = json_obj[self.pair]['low']
        self.avg = json_obj[self.pair]['avg']
        self.vol = json_obj[self.pair]['vol']
        self.vol_cur = json_obj[self.pair]['vol_cur']
        self.last = json_obj[self.pair]['last']
        self.buy = json_obj[self.pair]['buy']
        self.sell = json_obj[self.pair]['sell']
        