import pandas as pd

# Load dataset (iris.data has no header)
df = pd.read_csv("iris.data", header=None, names=[
    "sepal_length",
    "sepal_width",
    "petal_length",
    "petal_width",
    "class"
])

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

plt.scatter(df['sepal_length'], df['sepal_width'])
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.title("Iris Dataset Visualization")
plt.show()