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

# PS G:\pandas\Ex_Files_Python_Excel\Ex_Files_Python_Excel\Exercise Files> & C:/Users/or/AppData/Local/Programs/Python/Python37/python.exe "g:/pandas/Ex_Files_Python_Excel/Ex_Files_Python_Excel/Exercise Files/filter.py"
#  Region  Units  Sales  Export
# 0  South     54    332     100
# 1  North     20    110      50
# # 2   East     36    224      85
# 3   West     60    400     110
# 4   West     50    226      65
# 5  North     84    470     150
#                      0         1                                 2            3    4      5       6
# 0                 John       Doe                 120 jefferson st.    Riverside   NJ   8074   45000
# 1                 Jack  McGinnis                      220 hobo Av.        Phila   PA   9119   18000
# 2        John "Da Man"    Repici                 120 Jefferson St.    Riverside   NJ   8075  120000
# 3              Stephen     Tyler  7452 Terrace "At the Plaza" road     SomeTown   SD  91234   90000
# 4                  NaN  Blankman                               NaN     SomeTown   SD    298   30000
# 5  Joan "Danger", Anne       Jet               9th, at Terrace plc  Desert City   CO    123   68000
#                 ID  EGF_Baseline  EGF_Stimulus
# 0      FBgn0029994         -1.25         -0.27
# 1      FBgn0037191         -1.05          0.78
# 2      FBgn0036810          2.08          1.34
# 3      FBgn0033320          1.15          0.45
# 4      FBgn0051156         -1.77         -0.76
# ...            ...           ...           ...
# 11761  FBgn0026136          0.57          1.23
# 11762  FBgn0037356          1.14         -0.95
# 11763  FBgn0038214         -1.86         -0.67
# 11764  FBgn0042110          1.49          0.43
# 11765  FBgn0034202         -1.32         -0.22

# [11766 rows x 3 columns]
