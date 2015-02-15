#bitstamp setup
#Taylor Webber

from urllib2 import urlopen
import json

url = 'https://www.bitstamp.net/api/ticker/'

response = urlopen(url)
json_obj = json.load(response)

# Uncomment to view JSON output from API   
#f = open('output_bitstamp.json', 'w')
#f.write(json.dumps(json_obj, indent=4))
#f.close()

class BitStampTicker:
    def __init__(self):
        response = urlopen(url)
        json_obj = json.load(response)
        
        self.last = json_obj['last']
        self.bid = json_obj['bid']
        self.high = json_obj['high']
        self.low = json_obj['low']
        self.ask = json_obj['ask']
        
    def update_ticker(self):
        response = urlopen(url)
        json_obj = json.load(response)
        
        self.last = json_obj['last']
        self.bid = json_obj['bid']
        self.high = json_obj['high']
        self.low = json_obj['low']
        self.ask = json_obj['ask']
        