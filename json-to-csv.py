import json
import pandas as pd
from pandas.io.json import json_normalize

f = open('citylots.json') # open the json file
data = json.load(f) # load as json
f.close()

df = json_normalize(data['features']) #load json into dataframe
df.to_csv('json-to-csv.csv', sep=',', encoding='utf-8') #save as csv