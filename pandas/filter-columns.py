import pandas as pd
from openpyxl.workbook import Workbook

df = pd.read_csv(r'G:\pandas\Ex_Files_Python_Excel\Ex_Files_Python_Excel\Exercise Files\Names.csv', header=None)
df.columns = ['First', 'Last', 'Address', 'City', 'State', 'Area Code', 'Number' ]

print(df)
print(df[['Last', 'Area Code']])
print('------------------------------------')
# Print only 3 rows
print(df['Last'][0:3])
print('------------------------------------')
print('------------ iloc ------------------')
# Print all raw 3
print (df.iloc[3])
# 2        John "Da Man"    Repici                 120 Jefferson St.    Riverside    NJ       8075  120000
print (df.iloc[2,1])
# output will be:
# Repici
# Now you can see we have both the State and the Area Code and their appropriate indices.
#  Now they only tricky thing to remember here is that we use double brackets because we're 
# presenting the index of the data frame as a list of columns.
