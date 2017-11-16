import sys
import json
from pprint import pprint

with open('torrentData.json') as data_file:    
    jsonData = json.load(data_file)

total_results = int(jsonData["data"]["movie_count"])
if total_results > 0:
    print(str( jsonData["data"]["movies"][0]["torrents"][0]["hash"] ))
    #print(str( jsonData["list"][0]["torrentLink"] ))
#cmdargs = str(sys.argv)

#print(str(sys.argv[1]))
