import pandas as pd

df = pd.DataFrame({'date': ['2016-6-10 20:30:0', 
                            '2016-7-1 19:45:30', 
                            '2013-10-12 4:5:1'],
                   'value': [2, 3, 4]})df['date'] = pd.to_datetime(df['date'], format="%Y-%d-%m %H:%M:%S")

