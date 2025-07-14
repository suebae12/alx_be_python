
# finance_calculator.py

# User Input for Financial Details
income = int(input("Enter your monthly income: "))
expenses = int(input("Enter your total monthly expenses: "))

# Calculate Monthly Savings
monthly_savings = income - expenses

# Project Annual Savings:
# Assume a simple annual interest rate of 5%.
# Use the simplified formula: 
# Projected Savings = Monthly Savings * 12 + (Monthly Savings * 12 * 0.05)
annual_savings = monthly_savings * 12
interest = annual_savings * 0.05
projected_savings = annual_savings + interest

# Output Results
print(f"Your monthly savings are ${int(monthly_savings)}.")
print(f"Projected savings after one year, with interest, is: ${int(projected_savings)}.")
