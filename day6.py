# ---1. Basic error handling---
try:
    numerator = 100
    denomintor = 0
    result = numerator / denomintor
    print("Result:", result)
except ZeroDivisionError:
    print("Handle errror: cannot divide a no by zero")

print("execution continues normally without crashing.")

#--- 2. Built-in Modules---
import math
import random 

# Math operation s
print("square root of 64:", math.sqrt(64)) 
print("factorial of 5:", math.factorial (5))

# random sampling  (e.g. , simulating 5 daily website visits)
daily_visits = [random.randint(100, 500) for _ in range(5)]
print ("Simulated daily Traffic:", daily_visits)

# --- 3. MINI PROJECT ---
#==========================================
# Day 6: Error Handling and Modules
# ==========================================
import math 
# simulated raw incoming data from an external source
raw_record = [
    {"name": "Saloni", "score": "95"},
    {"name": "Amit", "score": "82"},
    {"name": "Vikas", "score": "absent"},  # Invalid numeric value
    {"name": "Pooja", "score": "88"},
    {"name": "Rohan", "score": "N/A"},     # Invalid numeric value
]
valid_scores = []

print("--- processing data stream ----")
for record in raw_record:
    try:
        clean_score = int(record["score"])
        valid_scores.append(clean_score)
        print(f"Accepted: {record['name']} -> {clean_score}")
    except ValueError:
        print(f"Skipped invalid record for {record['name']}: '{record['score']}'")

if valid_scores:
    avg = sum(valid_scores) / len(valid_scores)
    print("\n--- Summary Metrics ---")
    print(f"Valid Records Parsed: {len(valid_scores)}")
    print(f"Class Average Score:  {round(avg, 2)}")