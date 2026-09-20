import pandas as pd

# 1. Creating a dataframe from a dictionary (like a small table)
data = {
    "Product": ["Laptop", "Mouse", "Keyboard", "Monitor"],
    "Price": [800, 25, 45, 150],
    "Stock": [15, 120, 50, 30]
}
df = pd.DataFrame(data)

print("--- Smart Store Invertory---")
print(df)

# 2. Checking structural health and data types using info()
print("\n--- Summary Info (Data Health Check) ---")
print(df.info())

# 3. Selecting a single column (returns a Pandas Series)
print("--- Product column")
print(df["Product"])

# 4. Selecting multiple columns
print("--- Product column and Price ---")
print(df[["Product", "Price"]])

# 5. Filtering data (e.g., products with a price greater than $50)
print("\n--- Expensive Products (Price > 50) ---")
expensive_products = df[df["Price"] >50]
print(expensive_products)

# 6. Basic statistical summary of numerical columns
print("\n--- Statistical Summary ---")
print(df.describe())

# 6. Saving your dataframe to a csv file
df.to_csv("store_inventory.csv", index=False)
print("DataFrame successfully saved to 'store_inventory.csv'!")

# 7. Reading data back from a CSV file
loaded_df = pd.read_csv("store_inventory.csv")

print("\n--- Loaded Data from CSV ---")
print(loaded_df)