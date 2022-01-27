import pandas as pd
date='2020/11/26 12:00:00'
date_time=pd.to_datetime(date, format='%Y/%m/%d %H:%M:%S')
print(date_time)

date='2020/11/26 12:00:00'
date_time=pd.to_datetime(date, format='%Y/%m/%d %H:%M:%S')
print(date_time.strftime('%d-%m-%Y'))
# Best time format solution from codegrepper.com