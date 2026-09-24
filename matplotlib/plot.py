import pandas as pd
import matplotlib.pyplot as plt

# 1. sample data( weekly sales trend)
data = {
    "Days": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun" ],
    "Sales": [120, 190, 150, 220, 280, 340, 310]
}
df = pd.DataFrame(data)

# 2. Line plot with customization
plt.plot(df["Days"], df["Sales"], color="green", marker="o", linewidth=2, linestyle="--")

# 3. Add Titles and Labels
plt.title("Weekly  Sales Trend", fontsize=14, fontweight="bold")
plt.xlabel("Days of the week", fontsize=12)
plt.ylabel("Sales Amount ($)", fontsize=12)

# 4. Enable Grid for better readability
plt.grid(True, linestyle=":", alpha=0.7)

# 5. display the graph
plt.show()