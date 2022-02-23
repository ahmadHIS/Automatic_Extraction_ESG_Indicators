import os

import pandas
import pandas as pd

directory = os.path.join("D:\HIS\HisProject\\refinedTable")
tempPath = "E:\HIS\HisProject\\refinedTable\BD_Sustainability-report-2020_EN6.csv"
for root, dirs, files in os.walk(directory):
    for file in files:
        path = "D:\HIS\HisProject\\refinedTable" + "\\" + file

        df = pd.read_csv(path)
        df = df.drop(df[df.isnull().sum(axis=1) > len(df.columns) / 2].index)

        pandas.set_option('display.max_rows', None)
        pd.options.display.width = 0
        print(df)
        print("################## Report Finish ###################")
        break
    break



