# Create the LP problem: Maximize profit
prob = pulp.LpProblem("Furniture_Production", pulp.LpMaximize)

# Decision variables: Non-negative integers (assuming whole units)
chairs = pulp.LpVariable("Chairs", lowBound=0, cat='Integer')
tables = pulp.LpVariable("Tables", lowBound=0, cat='Integer')

# Objective function: Maximize profit = 8*Chairs + 12*Tables
prob += 8 * chairs + 12 * tables, "Total_Profit"

# Constraints
# Labor: 2*Chairs + 3*Tables <= 120
prob += 2 * chairs + 3 * tables <= 120, "Labor_Constraint"

# Wood: 4*Chairs + 6*Tables <= 180
prob += 4 * chairs + 6 * tables <= 180, "Wood_Constraint"

# Display the problem formulation (for verification)
print(prob)