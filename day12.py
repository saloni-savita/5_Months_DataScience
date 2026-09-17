import numpy  as np
# 1. Element-wise Vectorized Operations (No loops  needed)
prices = np.array([100, 200, 300, 400])
quantities = np.array([2, 1, 3, 2])

# Multiplying matching elements  instantly
total_cost = prices * quantities
print("Total cost per item:", total_cost)

# Adding a flat tax to all prices at once
new_prices = prices + 50
print("Prices after tax:", new_prices)

# 2. Universal Functions(Ufuncs)
numbers = np.array([1, 4, 9, 16])
print("*\nSquare  Roots:", np.sqrt(numbers))

# 3. Axis-wise Calculations (The Matrix Magic)
# Let's create a 2D matrix of scores (2 rows, 3 columns)
matrix = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print("\n--- Original Matrix---")
print(matrix)

# Total summ of every single element
print("Total Sum aixs=0 (Columns):", np.sum(matrix, axis=0))

# axis=0 -> Downwardss (column-wise sum)
print("Sum along axis=0 (Columns):", np.sum(matrix, axis=0))

# axis=1 -> Horizontally (Row-wise sum)
print("Sum along axis=1 (Rows):", np.sum(matrix, axis=1))
