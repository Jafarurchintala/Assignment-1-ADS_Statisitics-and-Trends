# Import necessary python packages
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Read the dataset
data = pd.read_csv('financials.csv')

# Display the dataset
print(data)

# Check if missing values are there
print(data.isnull().sum())

# Drop columns 'Symbol' and 'SEC Filings'
data = data.drop(['Symbol', 'SEC Filings'], axis="columns")

# Sorting data by 'Price' in descending order
data = data.sort_values(by=['Price'], ascending=False)

# Display the sorted data
print(data.head())

# Function to plot the line chart
def line():
    plt.figure()
    plt.plot(data['Name'][:20], data['52 Week Low'][:20], color='blue', label='low')
    plt.plot(data['Name'][:20], data['52 Week High'][:20], color='red', label='high')
    plt.xlabel('Company Name')
    plt.ylabel('Price in GBP')
    plt.legend()
    plt.title('Highest and Lowest price in last 52 weeks of top 20 companies')
    plt.xticks(rotation=90)
    plt.show()

# Function to plot the bar chart
def barplot():
    plt.figure()
    plt.bar(data['Name'][:10], data['Price/Earnings'][:10])
    plt.xlabel('Company Name')
    plt.ylabel('Price in GBP')
    plt.title('Price/Earnings of top 10 companies')
    plt.xticks(rotation=90)
    plt.show()

# Function to plot the heatmap
def heatmap():
    # Selecting numeric columns
    numeric_data = data.select_dtypes(include=np.number)
    # Calculating correlation matrix
    corr_matrix = numeric_data.corr()
    # Plotting the heatmap
    plt.figure(figsize=(10, 8))
    plt.title('Correlation Heatmap')
    plt.imshow(corr_matrix, cmap='coolwarm', interpolation='nearest')
    plt.colorbar()
    plt.xticks(range(len(corr_matrix.columns)), corr_matrix.columns, rotation=90)
    plt.yticks(range(len(corr_matrix.columns)), corr_matrix.columns)
    plt.show()  

# Call plotting functions
line()
barplot()   
heatmap()
