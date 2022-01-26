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
# Print raw 3
print (df.iloc[3])
# Now you can see we have both the State and the Area Code and their appropriate indices.
#  Now they only tricky thing to remember here is that we use double brackets because we're 
# presenting the index of the data frame as a list of columns.


# Output ============================================
#                   First      Last                           Address         City State  Area Code  Number
# 0                 John       Doe                 120 jefferson st.    Riverside    NJ       8074   45000
# 1                 Jack  McGinnis                      220 hobo Av.        Phila    PA       9119   18000
# 2        John "Da Man"    Repici                 120 Jefferson St.    Riverside    NJ       8075  120000
# 3              Stephen     Tyler  7452 Terrace "At the Plaza" road     SomeTown    SD      91234   90000
# 4                  NaN  Blankman                               NaN     SomeTown    SD        298   30000
# 5  Joan "Danger", Anne       Jet               9th, at Terrace plc  Desert City    CO        123   68000
#        Last  Area Code
# 0       Doe       8074
# 1  McGinnis       9119
# 2    Repici       8075
# 3     Tyler      91234
# 4  Blankman        298
# 5       Jet        123
# ------------------------------------
# 0         Doe
# 1    McGinnis
# 2      Repici
# Name: Last, dtype: object
# ------------------------------------
# ------------ iloc ------------------
# First                                 Stephen
# Last                                    Tyler
# Address      7452 Terrace "At the Plaza" road
# City                                 SomeTown
# State                                      SD
# Area Code                               91234
# Number                                  90000
# Name: 3, dtype: object
