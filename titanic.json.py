import pandas as pd

# Load titanic.json (JSON Lines format)
df = pd.read_json("titanic.json", lines=True)

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

# If there are numeric columns, plot first two
numeric_cols = df.select_dtypes(include=["number"]).columns

if len(numeric_cols) >= 2:
    plt.scatter(df[numeric_cols[0]], df[numeric_cols[1]])
    plt.xlabel(numeric_cols[0])
    plt.ylabel(numeric_cols[1])
    plt.title("Titanic JSON Visualization")
    plt.show()
else:
    print("\nNot enough numeric columns to plot a scatter graph.")
