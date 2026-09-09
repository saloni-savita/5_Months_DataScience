multiply = lambda a , b :a*b
result = multiply(4,5)
print("product:", result)

# Step 1: Write data to a text file
with open("students.txt", "w") as file:
    file.write("Saloni,Data Science,92\n")
    file.write("Amit,Web Development,78\n")
    file.write("Pooja,Artificial Intelligence,88\n")

print("File created successfully.")

# Step 2: Read data from the file
with open("students.txt", "r") as file:
    lines = file.readlines()

print("File Content:", lines)


# ==========================================
# Day 5: File Handling and Lambda Functions
# ==========================================

# --- 1. Lambda Demonstration ---
# Categorizes a student as 'Pass' or 'Needs Improvement'
classify_grade = lambda score: "Pass" if score >= 80 else "Needs Improvement"


# --- 2. Write Raw Data (Simulated Database Export) ---
with open("students.txt", "w") as file:
    file.write("Saloni,Data Science,92\n")
    file.write("Amit,Web Development,78\n")
    file.write("Pooja,Artificial Intelligence,88\n")
    file.write("Vikas,Cloud Computing,65\n")


# --- 3. Read and Process Records (ETL Pipeline) ---
processed_records = []

with open("students.txt", "r") as file:
    for line in file:
        # .strip() removes whitespace and newlines (\n)
        # .split(",") breaks the comma-separated string into a list
        name, domain, score_str = line.strip().split(",")
        score = int(score_str)
        
        # Apply the lambda function
        status = classify_grade(score)
        
        # Store as a clean dictionary
        processed_records.append({
            "name": name,
            "domain": domain,
            "score": score,
            "status": status
        })


# --- 4. Display Results ---
print("--- Processed Student Records ---")
for record in processed_records:
    print(f"{record['name']} | {record['domain']} | Score: {record['score']} | Status: {record['status']}")