import pandas as pd

# Sample sales dataset with categories
data = {
    "Category": ["Electronics", "Stationery", "Electronics", "Stationery", "Electronics", "Furniture"],
    "Product": ["Laptop", "Pen", "Mouse", "Notebook", "Monitor", "Chair"],
    "Price": [800, 2, 25, 5, 150, 120],
    "QuantitySold": [10, 100, 50, 200, 15, 8]
}

df = pd.DataFrame(data)
print("--- Original Data ---")
print(df)

# 1. simple groupby: Total Quantity Sold per category
print("\n--- Total  Quantity Sold per category ---")
total_qty = df.groupby("Category")["QuantitySold"].sum()
print(total_qty)

# 2. Average Price per category
print("\n--- Average Price per category ---")
avg_price = df.groupby("Category")["Price"].mean()
print(avg_price)

# 3. Advanced Aggregation: Multiple stats at once using .agg()
print("\n--- Summary Report (Avg price & Total Quantity) ---")
summary_report = df.groupby("Category").agg({
    "Price": "mean",
    "QuantitySold": "sum"
})
print(summary_report)