import csv

import null as null
import numpy as np
import pandas
import pandas as pd

tempPath = "E:\HIS\HisProject\\refinedTable\FedEx_2021_ESG_Report6.csv"

df = pd.read_csv(tempPath)
df = df.drop(df[df.isnull().sum(axis=1) > len(df.columns) / 2].index)
pandas.set_option('display.max_rows', None)
pd.options.display.width = 0
df = df.reset_index()  # make sure indexes pair with number of rows
searchFor = ["scope 1"]
print(df)
for row in df.iterrows():
    #gives us turpel
    cellData = row
    # convert tupel in to list
    mylist = list(cellData)
    # convert list in to pandas data fram
    dataFrame1 = pd.DataFrame(mylist)
    # this logic will return us data fram of single row of type true false
    trueItems = dataFrame1.apply(lambda row: row.astype('str').str.contains('|'.join(searchFor)))
    dataFrame = pd.DataFrame(data=trueItems)
    numpy_array = dataFrame.to_numpy()
    result = np.count_nonzero(numpy_array)
    if result > 0:
        print("######## Selected Row #########")
        print(cellData)
