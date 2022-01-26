import pandas as pd
from openpyxl.workbook import Workbook

df = pd.read_csv('Names.csv', header=None)
df.columns = ['First', 'Last', 'Address', 'City', 'State', 'Area Code', 'Number' ]

print(df['Last'])
# comment test