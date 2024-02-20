import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_excel(r'./source.xlsx')

# Splitting the 'Local Areas' column into separate columns for each food program
df = df['Local Areas'].str.get_dummies(sep=',').groupby(level=0).sum()

# Transpose the DataFrame
df = df.T

# Plotting a stacked bar graph
plt.figure(figsize=(15, 10))  # Adjust the figure size as needed
df.plot(kind='barh', stacked=True, ax=plt.gca())  # Stacked horizontal bar plot

# Add labels and title
plt.xlabel('Local Area')  # Label for the x-axis
plt.ylabel('Number of Food Programs Offered')  # Label for the y-axis
plt.title('Low-Cost/ Free Food Available in Vancouver City')  # Title of the plot

# Show the plot
plt.show()