def calculate_interest(principle, rate, time):
    simple_interest = (principle * rate * time / 100)
    print(f"The simple interest for a principal amount of ${principal:,.2f} at an interest rate of {rate}% over a period of {time} years is: ${simple_interest:,.2f}")
    return simple_interest
principal = int(input("Enter the prinicpal amount:  "))
rate = int(input("Enter the interest rate as a whole number (5% would be 5):  "))
time = int(input("Enter the investment time in whole years:  "))
simple_interest = calculate_interest(principal, rate, time)