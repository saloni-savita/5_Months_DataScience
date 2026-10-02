import matplotlib.pyplot as plt

# 1. sample  data : Days of the week vs temperature 
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
temperature = [28, 30, 27, 32, 35]

# 2. create a line  plot
plt.plot(days, temperature, color='blue', marker='o', linestyle='-', linewidth=2)

# 3. give the graph a professional look with titles and labels
plt.title('Daily Temperature Trend')
plt.xlabel('Days of the week')
plt.ylabel('Temperature (°C)')

# 4. enable grid for better readability
plt.grid(True)

# 5. display the graph
plt.show()

