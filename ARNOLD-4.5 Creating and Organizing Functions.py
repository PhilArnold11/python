def factorial(n):
    if n == 1 or n == 0:#define base case
        return 1 #the factorial of 1 and 0 is 1
    else:#define recursive step
        return n*factorial(n-1)#n multiplied by a call to itself with n-1
def main():
    n = int(input('Enter a non-negative integer:  '))#prompt the user to enter non-negative integer
    factorial(n)#call the factorial function
    print (f'The factorial of {n} is {factorial(n)}')#use the users input as argument to factorial function
main()#call main function to run program
