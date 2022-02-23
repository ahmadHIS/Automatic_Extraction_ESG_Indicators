
companies = ["FBHS-ESG-Data-Sheet-FINAL", "ESG_Data_Center 2020-2015", "Texas Instruments summary",
             "Jacobs Engineering summary", "AWK",

             "ldan-esg-report", "BMY-2020-ESG-Report", "FedEx_2021_ESG_Report",
             "Freeport", "GenuineParts",
             "HollyCorp Summary Report"
    , "PCA_2020_Responsibility_Report summary", "BD_Sustainability-report-2020_EN",
             "GRI_preliminaryReport_v5", "hershey_sustainability_report",
             "western-digital-2020-sustainability-report"
    , "Boston_scientific_performance_report"]


import camelot
import numpy as np
import pandas as pd

str = ""
newPath="E:\HIS\HisProject\AllPdfs\\"
temp = "E:\HIS\HisProject\mPdfs\ESG_Data_Center 2020-2015.pdf"
for i in companies:
    mPath = newPath + i + ".pdf"
    tables = camelot.read_pdf(mPath, pages='all', flavor='stream')

    # tables.export(i + '.csv', f='csv', compress=True)
    refinedTableCounter = 0
    print(len(tables))
    print(i)
    for x in range(len(tables)):
        mTable = tables[x].df
        searchFor = ['Scope 1', 'CO2']
        trueItems = mTable.apply(lambda row: row.astype('str').str.contains('|'.join(searchFor)))
        dataFrame = pd.DataFrame(data=trueItems)
        numpy_array = dataFrame.to_numpy()
        result = np.count_nonzero(numpy_array)
        if result > 0:
            refinedTableCounter = refinedTableCounter + 1
            mTable.to_csv(f"{i}{refinedTableCounter}.csv")
            print("Consider this table")
