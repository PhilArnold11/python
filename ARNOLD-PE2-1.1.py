import random #import random module
random_number = random.randint(1, 100) #generate a random number between 1 and 100 using randit

def main(): #put the rest of the code in main function
    while True: # I used this link https://www.tutorialspoint.com/How-to-handle-a-python-exception-within-a-loop to help with the exception statement
        try: #use try statement
            guess = int(input('Guess a number between 1 and 100:  '))# allow user to enter a guess
            guess == random_number #compare guess to random number
            if guess == random_number: #if guess is correct the print statement will run and the loop will end with break statement
                print("You are correct!")
                break #loop continues unless user enters correct number
            elif abs(guess-random_number) < 5: #use abs function to calculate absolute difference between guess and the actual number
                print('Very Hot') #based on different provide specified responses to user
            elif abs(guess-random_number) < 15:
                 print('Hot')
            elif abs(guess-random_number) < 25:
                 print('Cool')
            elif abs(guess-random_number) > 25:
                 print('Cold')  
        except ValueError:#the except statement is looking for value error
                print('Please enter a valid number between 1 and 100')
main() #call main