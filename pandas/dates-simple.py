# importing pandas as pd
import pandas as pd

# change in date time format
date_sr = pd.to_datetime(pd.Series("2012-09-02"))
change_format = date_sr.dt.strftime('%d-%m-%Y')

# Print the formated date
print(change_format)