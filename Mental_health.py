# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load your dataset into a pandas DataFrame
# For example, if your dataset is a CSV file, you can use pd.read_csv("your_data.csv")
# If it's in a different format, adjust the function accordingly
df = pd.read_csv("mental_health_finaldata_1.csv")

# Display basic information about the DataFrame
print("DataFrame Information:")
print(df.info())

# Display descriptive statistics
print("\nDescriptive Statistics:")
print(df.describe())

# Explore your data and perform additional analysis
# For example, you can display the first few rows of the DataFrame
print("\nFirst few rows of the DataFrame:")
print(df.head())

# Plot a histogram of a numerical column
# Replace 'column_name' with the actual column you want to visualize
plt.figure(figsize=(10, 6))
plt.hist(df['Gender'], bins=20, color='skyblue', edgecolor='black')
plt.title('Histogram of Gender')
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.show()
