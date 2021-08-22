import pandas as pd
import os

def process_df(df):
    df.dropna(subset = ["楼层"], inplace=True)
    df.dropna(subset = ["详细地址"], inplace=True)
    df['full contact'] = df['联系人'] +' '+ \
        df['联系方式'].astype(str)+' '+ \
        df['楼层']
    

directory_in_str = 'F:\workspace\locations_display\inputs'
directory = os.fsencode(directory_in_str)
print(directory)
result = list()
cols = ['full contact', '详细地址']
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    print(filename)
    if filename.endswith(".xlsx"): 
        file_path = os.path.join(directory.decode("utf-8"), filename)
        xls = pd.ExcelFile(file_path)
        df = xls.parse(0)
        #print(df.columns)
        process_df(df)
        print(df)
        result+=df[cols].values[1:].tolist()
    else:
        continue
print(result)
print('https://jsfiddle.net/user/elifehacker/fiddles/')