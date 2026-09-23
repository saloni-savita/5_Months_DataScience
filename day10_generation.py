import numpy as np

# 1 . Quick matrix builders
zeros_matrix = np.zeros((3, 4))
ones_matrix = np.ones((2, 3), dtype=int)
identity_matrix = np.eye(3)

print("--- Generated Arrays ---")
print("Zeros Matrix (3x4):\n", zeros_matrix)
print("Ones Matrix (2x3):\n", ones_matrix)
print("Identity Matrix (3x3):\n", identity_matrix)

# 2. sequential data: np.arange() vs np.linspace()
range_arr = np.arange(10, 50, 5)
print("\nArange (step = 5):" , range_arr)

linear_points = np.linspace(0, 1, 5)
print("Linspace (5 points between 0 and 1):", linear_points)

# 3. random number simulation (synthetic data)
np.random.seed(42)
salaries = np.random.randint(5000, 150000, size=5)
print("\nsimulated salaries:", salaries)

# 4. handling missing values (NaN)
salaries_with_nan = salaries.astype(float)
salaries_with_nan[1] = np.nan

print("\nArray with NaN:", salaries_with_nan)
print("Standard np.mean() ->", np.mean(salaries_with_nan))
print("Clean np.nanmean()  ->", np.nanmean(salaries_with_nan))












