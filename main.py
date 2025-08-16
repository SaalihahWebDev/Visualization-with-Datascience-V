import pandas as pd
import  matplotlib.pyplot as plt
import seaborn as sns

# Sample dataset
data = {
    'City' : ['Karachi', 'Islamabad', 'Lahore', 'Faisalabad', 'Quetta'],
    'Size_sqft' : [1200, 900, 1100, 1000, 950],
    'Rent' : [30000, 25000, 28000, 27000, 24000],
}

df = pd.DataFrame(data)

# Create a figure with 2 subplots (side by side)
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# --- BAR GRAPH ---
sns.barplot(x='City', y='Rent', data=df, palette='dark', ax=axes[0])
axes[0].set_title('House Rent per City')
axes[0].set_ylabel('Rent (PKR)')

# --- PIE CHART ---
axes[1].pie(df['Rent'], labels=df['City'], autopct='%1.1f%%',startangle=90)
axes[1].set_title('Share of Rent by City')

plt.tight_layout()
plt.show()