import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

data = pd.read_csv('data.csv')

qualitative = data.iloc[:, 3:12]
quantitative = data.iloc[:, 12:22]

quantitative.columns = ['I am more productive','I am less frustrated','I am more fulfilled','I am more focused and satisfied', 'I am faster in repetitive tasks', 'I am more in the flow','I spend less time searching for information', 'I use less mental effort']

quantitative[['I am less frustrated','I spend less time searching for information','I use less mental effort']] = quantitative[['I am less frustrated','I spend less time searching for information','I use less mental effort']].apply(lambda x: 10-x, axis=1)


means = quantitative.mean().round(1).apply(lambda x: x*10)

print(means)
print(means.iloc[0:1])
productivity = means.iloc[0:1]
sat_wellbeing = means.iloc[1:4]
efficiency = means.iloc[4:7]

def to_percentage(x, pos):
    return f'{int(x)}%'

formatter = FuncFormatter(to_percentage)

# Define colors for each graph
colors_productivity = 'skyblue'
colors_satisfaction_wellbeing = 'lightgreen'
colors_efficiency = 'salmon'

# Productivity
fig1, ax1 = plt.subplots(figsize=(16,3))
ax1.barh(productivity.index, productivity, color=colors_productivity)
ax1.set_title('Productivity')
ax1.set_xlim(0, 100)
ax1.set_xlabel('Mean Score')
ax1.set_yticklabels(quantitative.columns)
ax1.xaxis.set_major_formatter(formatter)

# Satisfaction & Wellbeing
fig2, ax2 = plt.subplots(figsize=(16,4))
ax2.barh(sat_wellbeing.index, sat_wellbeing, color=colors_satisfaction_wellbeing)
ax2.set_title('Satisfaction & Wellbeing')
ax2.set_xlim(0, 100)
ax2.set_xlabel('Mean Score')
ax2.set_yticklabels(sat_wellbeing.index)
ax2.xaxis.set_major_formatter(formatter)

# Efficiency
fig3, ax3 = plt.subplots(figsize=(16,6))
ax3.barh(efficiency.index, efficiency, color=colors_efficiency)
ax3.set_title('Efficiency')
ax3.set_xlim(0, 100)
ax3.set_xlabel('Mean Score')
ax3.set_yticklabels(efficiency.index)
ax3.xaxis.set_major_formatter(formatter)

nps = qualitative.iloc[:, 0:1]


print(nps.value_counts().sort_index())
