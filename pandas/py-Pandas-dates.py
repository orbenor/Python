# Import Pandas package
from email.utils import format_datetime
import pandas as pd
# https://www.geeksforgeeks.org/how-to-change-the-pandas-datetime-format-in-python/  
# Create a sample dataframe
df = pd.DataFrame({'num_posts': [4, 6, 3, 9, 1, 14, 2, 5, 7, 2],
                   'date' : ['09-08-2020', '25-08-2020', '05-09-2020', 
                            '12-09-2020', '29-09-2020', '15-10-2020', 
                            '21-11-2020', '02-12-2020', '10-12-2020', 
                            '18-12-2020']})
                   #'date' : ['2020-08-09', '2020-08-25', '2020-09-05', 
                   #         '2020-09-12', '2020-09-29', '2020-10-15', 
                   #         '2020-11-21', '2020-12-02', '2020-12-10', 
                   #         '2020-12-18']})
rslt_df = df.sort_values(by = 'date')
print(rslt_df)

df = pd.DataFrame({'num_posts': [4, 6, 3, 9, 1, 14, 2, 5, 7, 2,15],
                   'date' : ['9-8-2020', '2-9-2020', '5-9-2020',
                             '12-9-2020', '29-9-2020', '15-10-2020', 
                             '21-11-2020', '2-12-2020', '17-12-2020',
                             '18-12-2020','19-12-2020']})

#rslt_df = df.sort_values(by = 'date', format="%d%%m%Y")
# print(rslt_df)
print('-----------------------------')
df = pd.DataFrame({"value": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17,18, 19, 20] , "date": ["2019-3-18", "2019-10-24", "2019-1-1", "1-1-2018", "29-1-2018", "9-8-2020", "2-9-2020", "5-9-2020",
                             "12-9-2020", "29-9-2020", "15-10-2020", 
                             "21-11-2020", "2-12-2020", "17-12-2020",
                             "18-12-2020","19-12-2020", "21-12-2020", "12-2-2020", "27-2-2022", "12-1-2022"]})
df["date"] = pd.to_datetime(df["date"])

df = df.sort_values(by = "date")
formatted_df = df["date"].dt.strftime("%#d/%#m/%Y")
print (formatted_df)
