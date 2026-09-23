import pandas as pd 
import matplotlib.pyplot as plt

# Data
data = {
    "Month":["jan", "feb", "mar"],
    "Sales": [1200, 1500, 1100]
}
df = pd.DataFrame(data)

# Bar chart 
df.plot(x="Month", y="Sales", kind="bar", title="Monthly Sales")

# show the graph of this window
plt.show()