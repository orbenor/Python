import pandas as pd
from openpyxl.workbook import workbook
df_excel = pd.read_excel ('regions.xlsx')
df_csv = pd.read_csv ('Names.csv', header=None)
df_txt = pd.read_csv ('data.txt', delimiter='\t')

print(df_excel)
print(df_csv)
print(df_txt)

df_csv.columns = ['First', 'Last', 'Addess', 'City', 'State', 'Area Code', 'Number']
df_csv.to_excel('modified-02.xlsx')
