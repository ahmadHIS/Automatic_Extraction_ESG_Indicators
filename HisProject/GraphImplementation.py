import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("D:\HIS\HisProject\co2plot.csv")
columnname=['Fortune Brands Carbon Emission',
       'General Motors Carbon Emission', 'Texas Instruments Carbon Emission',
       'Jacobs Engineering summary', 'American Water',
       'Gildan Carbon Emission', 'Bristol Meyers Carbon Emission',
       'Unnamed: 8', 'FreePort Carbon Emission',
       'Genuine Parts Carbon Emission']

years = [2015,2016,2017,2018,2019,2020]

X = ['Group A', 'Group B', 'Group C', 'Group D']
Ygirls = [10, 20, 20, 40]
Zboys = [20, 30, 25, 30]
dboys = [10, 20, 40, 21]

X_axis = np.arange(len(X))

plt.bar(X_axis - 0.2, Ygirls, 0.4, label='Girls')
plt.bar(X_axis + 0.3, Zboys, 0.4, label='Boys')
plt.bar(X_axis + 0.6, dboys, 0.4, label='No Gender')

plt.xticks(X_axis, X)
plt.xlabel("Groups")
plt.ylabel("Number of Students")
plt.title("Number of Students in each group")
plt.legend()
plt.show()