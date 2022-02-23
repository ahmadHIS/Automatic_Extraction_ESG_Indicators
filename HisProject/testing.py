import os

companies = ["FBHS-ESG-Data-Sheet-FINAL", "ESG_Data_Center 2020-2015", "Texas Instruments summary",
             "Jacobs Engineering summary", "AWK",
             "Gildan", "BristolMeyers", "FedEx_2021_ESG_Report",
             "Freeport", "GenuineParts",
             "HollyCorp Summary Report"
    , "PCA_2020_Responsibility_Report summary", "BD_Sustainability-report-2020_EN",
             "GRI_preliminaryReport_v5", "hershey_sustainability_report",
             "western-digital-2020-sustainability-report"
    , "Boston_scientific_performance_report", "Carrier", "Cboe", "CenterPoint", "CharlesRiver", "ChurchDwight",
             "comcast", "csx", "entergy"]

import camelot
import numpy as np
import pandas as pd

temp = "E:\HIS\HisProject\AllPdfs\Boston_scientific_performance_report.pdf"
tables = camelot.read_pdf(temp, pages='all', flavor='stream')
tables.export("Boston_scientific_performance" + '.csv', f='csv', compress=True)
refinedTableCounter = 0
print("Total Table Found in Report")
print(len(tables))
for x in range(len(tables)):
    mTable = tables[x].df
    searchFor = ['Scope 1', 'CO2']
    trueItems = mTable.apply(lambda row: row.astype('str').str.contains('|'.join(searchFor)))
    dataFrame = pd.DataFrame(data=trueItems)
    numpy_array = dataFrame.to_numpy()
    result = np.count_nonzero(numpy_array)
    if result > 0:
        refinedTableCounter = refinedTableCounter + 1
        mTable.to_csv(f"Boston_scientific_performance{refinedTableCounter}.csv")
        print("Consider this table")
