import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_excel(r'./source.xlsx')

# Get the counts of unique values in the 'Local Areas' column
# This implies the number of food programs available in a particular 'Local Area'
local_area_counts = df['Local Areas'].value_counts()

# Plotting
plt.figure(figsize=(15, 6))  # Adjust the figure size as needed
local_area_counts.plot(kind='barh')  # Horizontal bar plot
plt.xlabel('Number of Food Programs Offered')  # Label for the x-axis
plt.ylabel('Local Area')  # Label for the y-axis
plt.title('Low-Cost/ Free Food Available in Vancouver City')  # Title of the plot
plt.show()