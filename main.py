import pandas as pd
import matplotlib.pyplot as plt

# Dataset: U.S. Science/Tech Spending vs. Suicides by Suffocation
data = {
    'Year': list(range(2000, 2010)),
    'Science_Spending_Billions': [60, 65, 70, 75, 80, 90, 100, 110, 115, 120],
    'Suicides_by_Suffocation': [6000, 6300, 6700, 7200, 7600, 8500, 8800, 9100, 9400, 9500]
}

# Set up the pandas dataframe
df = pd.DataFrame(data)

# Create the plot thing
fig, ax1 = plt.subplots(figsize=(10, 5))

# Left axis for Science Spending
color = 'tab:blue'
ax1.set_xlabel('Year')
ax1.set_ylabel('Science/Tech Spending (Billions USD)', color=color)
ax1.plot(df['Year'], df['Science_Spending_Billions'], marker='o', color=color, label='Science/Tech Spending')
ax1.tick_params(axis='y', labelcolor=color)

# Right axis for Suicides by Suffocation and Hanging
ax2 = ax1.twinx()
color = 'tab:red'
ax2.set_ylabel('Suicides by Suffocation/Hanging', color=color)
ax2.plot(df['Year'], df['Suicides_by_Suffocation'], marker='s', linestyle='--', color=color, label='Suicides by Suffocation')
ax2.tick_params(axis='y', labelcolor=color)

# Title and layout for the graph things
plt.title('Correlation Between Science Spending and Suicides by Suffocation (2000–2009)')
fig.tight_layout()
plt.grid(True)
plt.show()
