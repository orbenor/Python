# importing pandas as pd
from datetime import date
import pandas as pd
  
# Creating the date series
date_sr = pd.Series(pd.date_range(
    '2019-12-1', periods=3, freq='M', tz='Asia/Calcutta'))
  
# Creating the index
ind = ['Day 1', 'Day 2', 'Day 3']
  
# set the index
date_sr.index = ind

change_format = date_sr.dt.strftime('%#d,%#m,%Y')


# Print the formated date
print(change_format)