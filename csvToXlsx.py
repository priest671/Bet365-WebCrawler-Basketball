from os import listdir
from os.path import isfile, join
import pandas as pd
import openpyxl

dir_path = "result/Bet365Data/live/"
file_path_list = [join(dir_path, i) for i in listdir(dir_path) if isfile(join(dir_path, i))]

for i in file_path_list:
    df = pd.read_csv(i)
    a = i.replace('.csv', '')
    df.to_excel(a+'.xlsx', index=False)