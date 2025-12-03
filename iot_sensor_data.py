import pandas as pd

# Load dataset (CSV file)
df = pd.read_csv("iot_sensor_data.csv")

# Display first 5 rows
print("First 5 rows of dataset:")
print(df.head())

# Display dataset information
print("\nDataset Summary:")
print(df.info())

# Display statistics
print("\nStatistics:")
print(df.describe())

import matplotlib.pyplot as plt

# Visualization example: first two numeric columns
# (similar to sepal_length vs sepal_width in Iris)
numeric_cols = df.select_dtypes(include=["number"]).columns

if len(numeric_cols) >= 2:
    plt.scatter(df[numeric_cols[0]], df[numeric_cols[1]])
    plt.xlabel(numeric_cols[0])
    plt.ylabel(numeric_cols[1])
    plt.title("IoT Sensor Data Visualization")
    plt.show()
else:
    print("\nNot enough numeric columns to plot a scatter graph.")
