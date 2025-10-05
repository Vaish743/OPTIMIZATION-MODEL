# Solve the problem
prob.solve()

# Check status
status = pulp.LpStatus[prob.status]
print(f"Optimization Status: {status}")

# Extract optimal values
optimal_chairs = pulp.value(chairs)
optimal_tables = pulp.value(tables)
optimal_profit = pulp.value(prob.objective)

print(f"\nOptimal Production:")
print(f"Chairs: {optimal_chairs}")
print(f"Tables: {optimal_tables}")
print(f"Total Profit: ${optimal_profit}")

# Shadow prices (dual values) for constraints - useful for insights
labor_shadow = prob.constraints["Labor_Constraint"].pi
wood_shadow = prob.constraints["Wood_Constraint"].pi
print(f"\nShadow Price for Labor: ${labor_shadow} (additional profit per extra hour)")
print(f"Shadow Price for Wood: ${wood_shadow} (additional profit per extra unit)")