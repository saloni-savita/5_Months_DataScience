import pandas as pd
import numpy as np

# 1. Creating a messy dataframe with missing values (NaN)
data = {
    "Product": ["Laptop", "Mouse", "Keyboard", "Monitor", np.nan],
    "Price": [800, 25, np.nan, 150, 300],
    "Stock": [15, 120, 50, np.nan, 10]
}

df = pd.DataFrame(data)

print("--- Original Messy Data ---")
print(df)

# 2. Check how many missing values exist per column
print("\n--- Missing Values Count ---")
print(df.isnull().sum())

# 3. filling missing values (e.g., filling missing Price with a default or mean)
# Here, we will fill missing Price with 0 or a placeholder, and Stock with 0)
df["Price"] = df["Price"].fillna(df["Price"].mean())
df["Stock"] = df["Stock"].fillna(0)

# 4. Dropping rows where the 'Product' name is missing entirely
df = df.dropna(subset=["Product"])

print("\n--- Cleaned Data ---")
print(df)

# 5. Adding a new calculated column (Total Inventory Value = Price * Stock)
df["Total_Value"] = df["Price"] * df["Stock"]

print("\n--- Data with New Calculated Column ---")
print(df)