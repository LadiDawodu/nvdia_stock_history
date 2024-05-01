import pandas as pd
import sys
sys.path.append('src/data')
from datetime import datetime

from conn import get_historical_data, url, headers, querystring

# Retrieve historical data
historical_data = get_historical_data(url, headers, querystring)

# iterate through historical_data
def process_historical_data(data):
        data_hist = []
        for entry in data['data']:
                id = entry['id']
                attributes = entry['attributes']
                date = attributes['as_of_date']
                open = attributes['open']
                close = attributes['close']
                high = attributes['high']
                low = attributes['low']
                volume = attributes['volume']
                
                # append historical_data to empty
                # data_hist dictionary
                data_hist.append({
                        'id': id,
                        'date': date,
                        'open': open,
                        'close': close,
                        'high': high,
                        'low': low,
                        'volume': volume
                })
        return data_hist
                
                

# Convert processed data to Dataframe

def create_dataframe(data):
        
        # convert dictionary to python DF
        df = pd.DataFrame(data)
        
        # sort data by date for better analysis
        df.sort_values(by='date', ascending=True, inplace=True)
        
        # reset indexing after sorting
        df.reset_index(drop=True, inplace=True)
        
        return df




data_hist = process_historical_data(historical_data)

df = create_dataframe(data_hist)





