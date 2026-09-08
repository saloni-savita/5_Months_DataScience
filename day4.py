# --- 1. Basic Function Definition ---
def calculate_tax(income, tax_rate=0.10):
    """Calculates tax based on income and tax rate."""
    tax_amount = income * tax_rate
    net_income = income - tax_amount
    return net_income

# Function calls
saloni_net = calculate_tax(85000)
amit_net = calculate_tax(60000, 0.15)

print(f"Saloni's Net Income: {saloni_net}")
print(f"Amit's Net Income: {amit_net}")

# --- 2. List Comprehensions ---
raw_salaries = [45000, 72000, 85000, 31000, 95000]

# Traditional loop equivalent in one line: [expression for item in iterable]
# Add a 10% bonus to every salary
bonus_salaries = [salary * 1.10 for salary in raw_salaries]
print("Salaries with 10% Bonus:", bonus_salaries)

# Filtering with conditions: [expression for item in iterable if condition]
# Extract only high earners (> 70,000)
high_earners = [salary for salary in raw_salaries if salary > 70000]
print("High Earners (>70k):", high_earners)

# --- 3. Mini Project: Grade Normalizer ---
raw_scores = [68, 74, 89, 45, 92, 58]

def normalize_scores(scores, grace_marks=5):
    """Adds grace marks capped at 100, then filters passing scores (>= 60)."""
    # Comprehension with min() to ensure scores don't exceed 100
    updated_scores = [min(score + grace_marks, 100) for score in scores]
    
    # Filter passing scores
    passed_scores = [score for score in updated_scores if score >= 60]
    return passed_scores

passing_grades = normalize_scores(raw_scores)
print("Qualified Passing Scores:", passing_grades)