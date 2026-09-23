import pandas as pd

# Table 1. Employee basic details
emp_info = {
    "EmpID": [101, 102, 103, 104],
    "Name": ["Aarav", "Saloni", "Tannu", "Rohan"]
}
df_emp = pd.DataFrame(emp_info)

# Table 2. Employee salaries
emp_salary = {
    "EmpID": [101, 102, 103, 104],
    "Salary": [50000, 45000, 700000, 55000]
}
df_sal = pd.DataFrame(emp_salary)

print("--- Employee Info Table ---")
print(df_emp)

print("---Employee Salary Table ---")
print(df_sal)

# 1. MERGE: Combining table using a common column (EmpID)
print("\n--- Merged Table (using pd.merge) ---")
merged_df = pd.merge(df_emp, df_sal, on="EmpID")
print(merged_df)


# 2. CONCAT: Stacking tables vertically  (adding more rows)
# Let's create a new batch of employees
extra_emp = {
    "EmpID": [105, 106],
    "Name": ["Rahul", "Vaishnavi"]
}
df_extra = pd.DataFrame(extra_emp)

print("\n--- Concatenated Table (Stacking Rows using pd.concat) ---")
combined_df = pd.concat([df_emp, df_extra], ignore_index=True)
print(combined_df)
