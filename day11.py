import numpy as np
# creating 1D array
arr =  np.array([10, 20, 30, 40, 50, 60, 70])

# 1. SINGLE ELEMENT INDEXING
print("First element(index 0):", arr[0])
print("First element(index -1):", arr[-1])

# 2. Slicing (Extracting a chunk -> start:stop)
print("Index 1 to 4:", arr[1:5])
print(" Start to index  4:", arr[:4])
print("Index 3 to the end:",  arr[3:])

# Creating a 2d matrix (3 rows, 3 columns)
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print("\n--- 2D Matrix ---")
print(matrix)
# Extracting a specific element: Row 1, Column 2 (which is the number 6)
print("Row 1, Col 2 element:", matrix[1, 2])   # Output: 6

# Extracting an entire Row (Row 0)
print("Entire first row:", matrix[0, :])       # Output: [1 2 3]

# Extracting an entire Column (Column 1)
print("Entire second column:", matrix[:, 1])   # Output: [2 5 8]

# Creating an array of numbers
arr = np.array([10, 25, 30, 45, 50, 65, 80])

# 1. Applying a condition creates a Boolean Mask (True/False array)
condition = arr > 40
print("Boolean (True/False):", condition) 


# 2. Passing the condition back into the array to get the actual values
filtered_data = arr[arr > 40]
print("Values greater than 40:", filtered_data) 


# 1. Creating a 1D array with 12 elements
arr_1d = np.arange(1, 13)
print("Original 1D Array:\n", arr_1d)

# 2. Reshaping into a 3x4 Matrix (3 rows, 4 columns)
matrix_3x4 = arr_1d.reshape(3, 4)
print("\nReshaped to 3x4 Matrix:\n", matrix_3x4)

# 3. Reshaping into a 2x6 Matrix (2 rows, 6 columns)
matrix_2x6 = arr_1d.reshape(2, 6)
print("\nReshaped to 2x6 Matrix:\n", matrix_2x6)

# Flattening the 3x4 matrix back to 1D
flat_arr = matrix_3x4.ravel()
print("\nFlattened back to 1D:", flat_arr)

