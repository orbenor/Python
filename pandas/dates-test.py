import pandas as pd
date='2020/11/26 12:00:00'
date_time=pd.to_datetime(date, format='%Y/%m/%d %H:%M:%S')
print(date_time)

date='2020/11/26 12:00:00'
date_time=pd.to_datetime(date, format='%Y/%m/%d %H:%M:%S')
print(date_time.strftime('%d-%m-%Y'))
# Best time format solution from codegrepper.com

date='2-4-2020'
date_time=pd.to_datetime(date)
print (date)
print(date_time.strftime('%#d-%#m-%Y'))
# https://www.codegrepper.com/search.php?q=python%20pandas%20date%20format