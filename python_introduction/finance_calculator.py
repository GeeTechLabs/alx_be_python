monthly_income = int(input("Enter your monthly income: "))
montly_expense = int(input("Enter your total monthly expenses: "))


monthly_savings = monthly_income - montly_expense

projected_Savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

print(f'Your monthly savings are ${str(monthly_savings)}.')
print(f'Projected savings after one year, with interest, is: ${str(int(projected_Savings))}.')