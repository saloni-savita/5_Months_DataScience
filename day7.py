# ==========================================
# Day 7: Capstone - Mini ETL Pipeline
# ==========================================

# 1. Lambda Transformation Function
apply_bonus = lambda score,  attendance: score + 5 if attendance >= 90 else score

# 2. Ingest Raw Messy Data (creating input file with dirty records)
raw_data = """Saloni,95,92
Amit,88,78
Vikas,absent,85
Pooja,92,89
Rohan,60,N/A"""

with open("students_input.txt", "w") as f:
    f.write(raw_data)

print("Step 1. Raw dataset generated successfully.\n")

# 3. Read and clean  corrupted Records
clean_students = []


with open("students_input.txt", "r") as f:
    lines = f.readlines()

for line in lines:
    parts = line.strip().split(",")
    name = parts[0]
    att_str = parts[1]
    score_str = parts[2]

    try:
        #cast string values to integers
        attendance = int(att_str)
        score =int(score_str)
        #apply business transformation via lambda
        final_score = apply_bonus(score, attendance)

        clean_students.append(f"{name} -> Final Score: {final_score}")
        print(f"Accepted: {name} (Bonus evaluated)")

    except ValueError:
        # Gracefully handle non-numeric values like 'absent' or 'N/A'
        print(f"Skipped corrupted row for: {name}")

# 4. Export Processed Data to Output File
with open("clean_output.txt", "w") as f:
    for record in clean_students:
        f.write(record + "\n")

print("\nStep 2: Clean data successfully written to 'clean_output.txt'!")


