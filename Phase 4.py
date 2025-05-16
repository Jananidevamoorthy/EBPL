import pandas as pd

import matplotlib.pyplot as plt



# Load CSV

df = pd.read_csv("2018Floor1.csv")



# Sample data

sample = df.iloc[:10]



# Bar Chart

plt.figure(figsize=(10, 5))

plt.bar(sample['Date'], sample['z1_Light(kW)'], color='red')

plt.xticks(rotation=45, ha='right')

plt.title('Bar Chart: z1_Light(kW)')

plt.xlabel('Date')

plt.ylabel('Power (kW)')

plt.tight_layout()

plt.savefig("bar_chart.png")

plt.close()



# Scatter Plot

plt.figure(figsize=(8, 5))

plt.scatter(sample['z1_Light(kW)'], sample['z1_Plug(kW)'], c='blue')

plt.title('Scatter Plot: z1_Light(kW) vs z1_Plug(kW)')

plt.xlabel('z1_Light(kW)')

plt.ylabel('z1_Plug(kW)')

plt.tight_layout()

plt.savefig("scatter_plot.png")

plt.close()
