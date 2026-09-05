#--- Day 3:Dictionaries (key-value pairs) ---
student = {
    "name" : "Saloni",
    "role" : "Data Analyst",
    "score" : 92,
    "city" : "Delhi"
}

# Access value via keys
print("Student Name:", student["name"])
print("Target Role:", student["role"])

# Updating existing data and adding new key
student["score"] = 95 # update existing score
student["tool"] = "python" # add new key-value pair
print("Updated profile:", student)

# Extracting keys and values separately
print(" All Keys:", list(student.keys()))
print(" All Values:", list(student.values()))

#--Day 3: sets(Removing Duplicates)---
raw_skills =["Python", "SQL", "Python", "Excel", "SQL","Tableau"]
# convert list to a set to automatically eliminate duplicates
unique_skills = set(raw_skills)
print("Unique Skills:", unique_skills)

# Fast membership check (Data science skill check)
print("Is python present?", "Python" in unique_skills)


#--- Mini Project : Student Performance Tracker ---
gradebook ={
    "Saloni" :[85, 90,92],
    "Amit" : [70, 65, 75],
    "Pooja" : [95, 98, 100]
}
 # calculate the average score for each student 
for student_name, marks in gradebook.items():
    # Compute arithmetic mean: total marks divided by number of subjects
    avg = sum(marks) / len(marks)

    # Categorize performance using conditional statements
    if avg >= 75:
        status = "Distinction"
    elif avg >= 50:
        status = "Pass"
    else:
        status = "Needs Improvement"

    # Display formatted results rounded to 2 decimal places
    print(f"{student_name} -> Average: {round(avg, 2)} | Status: {status}")

  # Track maximum score
    if avg > highest:
        highest = avg
        topper_name = student_name

# Announce the topper after all students have been evaluated
print(f"\n🏆 Class Topper: {topper_name} with an average of {round(highest_avg, 2)}")