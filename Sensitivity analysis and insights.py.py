# Slack values (unused resources)
labor_slack = prob.constraints["Labor_Constraint"].slack
wood_slack = prob.constraints["Wood_Constraint"].slack

# Create a summary DataFrame
summary = pd.DataFrame({
    'Resource': ['Labor Hours', 'Wood Units'],
    'Available': [120, 180],
    'Used': [
        2 * optimal_chairs + 3 * optimal_tables,
        4 * optimal_chairs + 6 * optimal_tables
    ],
    'Slack': [labor_slack, wood_slack],
    'Shadow Price': [labor_shadow, wood_shadow]
})

print("Resource Utilization Summary:")
print(summary)

# Insights (printed as text)
print("\nKey Insights:")
print("1. Optimal production: 30 Chairs and 20 Tables, yielding $360 profit.")
print("2. Labor is fully utilized (no slack), so it's the binding constraint.")
print("3. Wood has 60 units unused (slack), indicating excess supply.")
print("4. Shadow prices show: Hiring 1 more labor hour increases profit by $2.")
print("   Investing in more wood won't help (shadow price $0) - focus on labor efficiency.")
print("5. If wood cost drops or labor increases, re-run the model for updated optima.")
print("6. Business Recommendation: Prioritize labor optimization (e.g., automation or overtime).")