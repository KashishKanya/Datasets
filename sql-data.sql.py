import pandas as pd
import matplotlib.pyplot as plt

# Read SQL file as plain text
with open("sql-data.sql", "r", encoding="utf-8") as f:
    lines = f.readlines()

# Convert to DataFrame
df = pd.DataFrame(lines, columns=["text"])

# Display first 5 rows
print("First 5 rows of dataset:")
print(df.head())

# Display dataset information
print("\nDataset Summary:")
print(df.info())

# Display statistics
print("\nStatistics:")
print(df["text"].str.len().describe())

# Add a column for line length
df["length"] = df["text"].str.len()

# Scatter plot like your previous code
plt.scatter(df.index, df["length"])
plt.xlabel("Line Number")
plt.ylabel("Character Count")
plt.title("SQL Data Line Length Visualization")
plt.show()
