import pandas as pd

# Load dataset (text file)
df = pd.read_csv("ascii-art.txt", header=None, names=["text"])

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

# For visualization, we can plot line length (just like scatter)
df["length"] = df["text"].str.len()

plt.scatter(df.index, df["length"])
plt.xlabel("Line Number")
plt.ylabel("Character Count")
plt.title("ASCII Art Line Length Visualization")
plt.show()
