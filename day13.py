import numpy as np

# 1. A 2D matrix of item  prices across 2 stores(2 rows, 3 columns)
prices = np.array([
    [100, 200, 300],
    [150, 250, 350]
])

# 2. A 1D array representinng a specific discount for each  of the 3 columns
discounts = np.array([10, 20, 30])

# 3. Broadcasting in action:
# The 1D array (3 items) is automatically stretched/broadcasted
# down across the rows of the 2D matrix!
final_prices = prices - discounts 

print("Original Prices:\n", prices)
print("\nDiscounts applied per column:",discounts)
print("\nFinal Prices after Broadcasting:\n",final_prices)