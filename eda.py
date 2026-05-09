import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("netflix_titles.csv")

# ----------------------------
# BASIC INFO
# ----------------------------
print("Shape of dataset:", df.shape)
print("\nColumns:\n", df.columns)

# ----------------------------
# CHECK MISSING VALUES
# ----------------------------
print("\nMissing Values:\n", df.isnull().sum())

# ----------------------------
# DATA CLEANING
# ----------------------------
df['director'].fillna('Unknown', inplace=True)
df['cast'].fillna('Unknown', inplace=True)
df['country'].fillna('Unknown', inplace=True)
df['rating'].fillna('Unknown', inplace=True)
df.dropna(subset=['date_added'], inplace=True)

# ----------------------------
# VISUALIZATION
# ----------------------------
sns.set(style="whitegrid")

# Movies vs TV Shows
plt.figure()
df['type'].value_counts().plot(kind='bar')
plt.title("Movies vs TV Shows")
plt.show()

# Top 10 Countries
plt.figure()
df['country'].value_counts().head(10).plot(kind='bar')
plt.title("Top 10 Countries")
plt.xticks(rotation=45)
plt.show()

# Ratings Distribution
plt.figure()
df['rating'].value_counts().head(10).plot(kind='bar')
plt.title("Ratings Distribution")
plt.xticks(rotation=45)
plt.show()

