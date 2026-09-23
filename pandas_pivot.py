import pandas as pd

# Sample sales dataset across different regions and products
data = {
    "Region": ["North", "South", "North", "South", "North", "South"],
    "Product": ["Laptop", "Laptop", "Mouse", "Mouse", "Keyboard", "Keyboard"],
    "Sales": [1500, 1200, 300, 250, 400, 350],
    "UnitsSold": [2, 1, 10, 8, 5, 4]
}

df = pd.DataFrame(data)
print("--- Original Data ---")
print(df)

# 1.  Creating a Pivot Table
# Index = Rows, Columns = Columns, Values = What we want to calculate, Aggfunc = Math operation
print("\n--- Pivot Tables: Total Sales by Region and Product ---")
pivot_df = df.pivot_table(
    index="Region",
    columns="Product",
    values="Sales",
    aggfunc="sum"
)
print(pivot_df)

print("\n--- Advanced Pivot Tables:Sales & Units  sold ---")
advanced_pivot = df.pivot_table(
    index="Region",
    columns="Product",
    values=["Sales", "UnitsSold"],
    aggfunc="sum"
)
print(advanced_pivot)