import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Read the dataset
df = pd.read_csv("dataset/Zomato-data-.csv")
print(df.head())

# Cleanse the dataset
# Function to handle rate column: converts '4.1/5' to 4.1 and handles NaNs
def handleRate(value):
    value=str(value).split('/')
    value=value[0]
    return float(value)

# Apply the handleRate function to the 'rate' column
df['rate']=df['rate'].apply(handleRate)
print(df.head())

# Summary Statistics
print(df.describe())
df.info()

# Visualization: Count of restaurants by type
sns.countplot(x=df['listed_in(type)'])
plt.xlabel("Type of restaurant")


# Visualization: Total votes by restaurant type
grouped_data = df.groupby('listed_in(type)')['votes'].sum()
result = pd.DataFrame({'votes': grouped_data})
plt.plot(result, c='green', marker='o')
plt.xlabel('Type of restaurant')
plt.ylabel('Votes')


# Analysis: Find the restaurant with the maximum votes
max_votes = df['votes'].max()
restaurant_with_max_votes = df.loc[df['votes'] == max_votes, 'name']

print('Restaurant(s) with the maximum votes:')
print(restaurant_with_max_votes)

# Visualization: Count of restaurants offering online ordering
sns.countplot(x=df['online_order'])

# Visualization: Distribution of ratings
plt.hist(df['rate'],bins=5)
plt.title('Ratings Distribution')
plt.show()

# Visualization: Count of restaurants by approximate cost for two people
couple_data=df['approx_cost(for two people)']
sns.countplot(x=couple_data)

# Visualization: Boxplot of rate vs online order
plt.figure(figsize = (6,6))
sns.boxplot(x = 'online_order', y = 'rate', data = df)

# Visualization: Heatmap of restaurant type vs online order
pivot_table = df.pivot_table(index='listed_in(type)', columns='online_order', aggfunc='size', fill_value=0)
sns.heatmap(pivot_table, annot=True, cmap='YlGnBu', fmt='d')
plt.title('Heatmap')
plt.xlabel('Online Order')
plt.ylabel('Listed In (Type)')
plt.show()

