# Import for plotting
import matplotlib.pyplot as plt
import numpy as np

# Plot feasible region
x = np.linspace(0, 60, 100)  # Chairs from 0 to 60
y_labor = (120 - 2*x)/3      # Labor constraint
y_wood = (180 - 4*x)/6       # Wood constraint

plt.figure(figsize=(8,6))
plt.plot(x, y_labor, label='Labor Constraint (120 hrs)')
plt.plot(x, y_wood, label='Wood Constraint (180 units)')
plt.fill_between(x, 0, np.minimum(y_labor, y_wood), alpha=0.3, color='lightblue', label='Feasible Region')
plt.plot(optimal_chairs, optimal_tables, 'ro', markersize=10, label='Optimal Point')
plt.xlabel('Number of Chairs')
plt.ylabel('Number of Tables')
plt.title('Feasible Region and Optimal Solution')
plt.legend()
plt.grid(True)
plt.xlim(0, 60)
plt.ylim(0, 50)
plt.show()

# Profit at optimal point
print(f"Profit at optimal point ({optimal_chairs}, {optimal_tables}): ${optimal_profit}")