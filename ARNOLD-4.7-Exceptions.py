def square_number():
    try:#add exception handling
        number = input("Enter a number to square: ")
        squared_number = int(number) ** 2
        print(f"The square of {number} is {squared_number}.")
    except ValueError:#add exception handling
        print("Please enter an integer.")

square_number()
