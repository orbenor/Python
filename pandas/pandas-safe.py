import pandas as pd
from openpyxl.workbook import Workbook

df = pd.read_csv(r'G:\pandas\Ex_Files_Python_Excel\Ex_Files_Python_Excel\Exercise Files\Names.csv', header=None)
df.columns = ['First', 'Last', 'Address', 'City', 'State', 'Area Code', 'Number' ]

print(df)

wanted_values = df[['First', 'Last', 'State']]
stored = wanted_values.to_excel('State_location.xlsx', index=None)
print(wanted_values)
