import numpy as np 

# 1. standard python list vs  NumPy  array

score_list = [75, 82, 90, 65, 88]
score_arr = np.array(score_list)

print("Original Array:", score_arr)
print("Data type:", type(score_arr))

# 2. Vectorized Math(no loops required)
# A standard python list requires a loop or list comprehension to add 5 to each element.
# NumPy applies arithmetic operations directly acorss the entire array:
curved_scores = score_arr + 5
print("curved scores (+5):", curved_scores)

# 3. Basic aggregation (key analytical metrics)
print("\n--- Summary metrices---")
print("Average Score :", np.mean(score_arr))
print("highest score:", np.max(score_arr))
print("lowest score:", np.min(score_arr))
print("standard dev:", round(np.std(score_arr) , 2))

# 4. boolean  filtering (core data cleaning technique)
# filter and extract only score that are 80 or higher
high_scorers = score_arr[score_arr >= 80]
print("\nscorers >= 80:", high_scorers)

# 4. creating  a 2d array (3 students across 3 subjects: Math, Science, English)
# Rows = Students, Columns = Subjects
grades = np.array([
   [85, 90, 78],
   [70, 65, 80],
   [92, 88, 95]
])
print("2D Matrix:\n", grades)
print("Shape (Rows, Cols):", grades.shape)
print("Dimensions:", grades.ndim)

# 2. 2D Slicing: [row_index, col_index]
# Rule: Use ':' to select 'all'
print("\n--- Slicing & Indexing ---")
print("Student 0 Math score (Row 0, Col 0):", grades[0, 0])
print("All scores for Student 2 (Row 2):", grades[2, :])
print("Science scores for all students (Col 1):", grades[:, 1])

# 3. Axis-wise Aggregations (Crucial Concept!)
# axis=0 -> Down columns (Per Subject)
# axis=1 -> Across rows (Per Student)
print("\n--- Axis Operations ---")
subject_averages = np.mean(grades, axis=0)
print("Average score per subject (Math, Sci, Eng):", np.round(subject_averages,1))

student_totals = np.sum(grades, axis=1)
print("Total score per student:", student_totals)

# 4. Reshaping: Flattening and Re-structuring
# Total elements = 9 (3x3). Can reshape into 1x9 or 9x1.
flat_grades = grades.reshape(-1)
print("\nFlattened to 1D:", flat_grades)



