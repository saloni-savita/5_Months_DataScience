import pandas as pd
import matplotlib.pyplot as plt

# Sample Data: Experience vs Salary
data = {
    "Experience_Years":[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Salary_Thousands":[40, 45, 50, 65, 70, 85, 90, 105, 110, 130]
}
df = pd.DataFrame(data)

# 2. Scatter plot with customization
plt.scatter(df["Experience_Years"], df["Salary_Thousands"], color="purple", s=100, alpha=0.8)

# 3. Add Titles and Labels
plt.title("Experience vs Salary Correlation", fontsize=14, fontweight="bold")
plt.xlabel("Year of Experience", fontsize=12)
plt.ylabel("Salary ($ in thousands)", fontsize=12)

# 4. Enable Grid
plt.grid(True, linestyle="--", alpha=0.5)

# 5. Display the graph
plt.show()