import pandas as pd
import warnings
warnings.filterwarnings('ignore', category=UserWarning, module='openpyxl')
# pd.set_option('display.max_rows', None)
# Read Excel file


pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)
df = pd.read_excel('Hardware-Software.xlsx', usecols=['unit', 'License Until Date', 'Duration'])

#pd.to_datetime(df['License Until Date'].dt.strftime('%m/%d/%Y'))
#pd['License Until Date'] = pd['License Until Date'].pd.strftime('%d-%m-%Y')
data_new1 = df
data_new1['License Until Date'] = data_new1['License Until Date'].dt.strftime('%d/%m/%Y')
print("--------- print data_new1 ---------------")
print(data_new1)
print("--------- print data_new1 ---------------")
print(df)

print (df.columns.values)
df = pd.read_excel('Hardware-Software.xlsx')
print (df.columns.values)

# Outputs
#   Courses    Fee  Duration  Discount
#0    Spark  25000   50 Days      2000
#1   Pandas  20000   35 Days      1000
#2     Java  15000       NaN       800
#3   Python  15000   30 Days       500
#4      PHP  18000   30 Days       800
