def main():
    user_input = input("Enter a character:  ")#prompt user for input

    while len(user_input) !=1:#implement a loop to ensure the input is only one character
        print("Please enter exactly one character.")#explain the loop will continue until one character is given
        user_input = input("Enter a character:  ")

    ascii_value = ord(user_input)#convert to ASCII value
    print(f"The ASCII value of {user_input} is {ascii_value}")#print the ASCII value

main()