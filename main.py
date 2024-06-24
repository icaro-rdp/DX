import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

data = pd.read_csv('data.csv')

qualitative = data.iloc[:, 3:12]
quantitative = data.iloc[:, 12:22]

quantitative.columns = ['I am more productive','I am less frustrated','I am more fulfilled','I am more focused and satisfied', 'I am faster in repetitive tasks', 'I am more in the flow','I spend less time searching for information', 'I use less mental effort']

quantitative[['I am less frustrated','I spend less time searching for information','I use less mental effort']] = quantitative[['I am less frustrated','I spend less time searching for information','I use less mental effort']].apply(lambda x: 10-x, axis=1)


means = quantitative.mean().round(1).apply(lambda x: x*10)



def to_percentage(x, pos):
    return f'{int(x)}%'

formatter = FuncFormatter(to_percentage)

# Define colors for each graph
colors_productivity = 'skyblue'

# Productivity
fig1, ax1 = plt.subplots(figsize=(4,4))
bars = ax1.barh(means.index, means, color=colors_productivity)
ax1.set_title('Productivity')
ax1.set_xlim(0, 100)
ax1.set_xlabel('Mean Score')
ax1.set_yticklabels(means.index)
ax1.xaxis.set_major_formatter(formatter)

# Add labels inside or outside the bars based on their width
for bar in bars:
    width = bar.get_width()
    label_x_pos = width if width > 5 else width + 5  # Adjust 5 to a smaller number if your bars are very narrow
    ax1.text(label_x_pos, bar.get_y() + bar.get_height() / 2, f'{width}%', va='center', color='black' if width > 5 else 'blue')

plt.show()