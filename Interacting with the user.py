#Using input to gather monthly income and expenses
income = float(input('What is your total monthly income? '))
housing = float(input('How much do you spend on your mortgage each month? '))
utilities = float(input('How much do you spend on utilities each month? '))
groceries = float(input('How much do you spend on groceries each month? '))
transportation = float(input('How much do you spend on transportation each month? '))
healthcare = float(input('How much do you spend on health care each month? '))
personalcare = float(input('How much do you spend on personal care each month? '))
clothing = float(input('How much do you spend on clothing each month? '))
debt = float(input('How much additional debt do you have each month? '))

#This defines the percentage calulation
def calculate_percentage(amount, income):
    return (amount / income) * 100

#This portion of the code uses the calculate_percentage definition to calculate the percentage of each expense
housing_percentage = calculate_percentage(housing, income)
utilities_percentage = calculate_percentage(utilities, income)
groceries_percentage = calculate_percentage(groceries, income)
transportation_percentage = calculate_percentage(transportation, income)
healthcare_percentage = calculate_percentage(healthcare, income)
personalcare_percentage = calculate_percentage(personalcare, income)
clothing_percentage = calculate_percentage(clothing, income)
debt_percentage = calculate_percentage(debt, income)

#The program prints the output of the previous calculation as a string displaying the results to the user.
print('\nBudget Breakdown')
print(f"Housing: {housing_percentage:.2f}%")
print(f'Utilities: {utilities_percentage:.2f}%')
print(f'Groceries: {groceries_percentage:.2f}%')
print(f'Transportation: {transportation_percentage:.2f}%')
print(f'Health Care: {healthcare_percentage:.2f}%')
print(f'Personal Care: {personalcare_percentage:.2f}%')
print(f'Clothing: {clothing_percentage:.2f}%')
print(f'Debt: {debt_percentage:.2f}%')