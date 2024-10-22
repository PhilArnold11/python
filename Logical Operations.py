num1 = float(input('Enter an integer: '))
num2 = float(input('Enter another integer: '))
#using the and operator to determine if both integers are greater than 0
if num1>0 and num2>0:
    print('Both numbers are greater than 0: True\n')
else:
    print('Both numbers are greater than 0: False\n')

#using the and operator to determine if both integers are greater than 100
if num1>100 and num2>100:
    print('Both numbers are greater than 100: True\n')
else: print('Both numbers greater than 100: False\n')

#using the or operator to determine if one of the integers is even
if num1%2==0 or num2%2==0:
    print('Either number is even: True\n')
else:
    print('Either number is even: False\n')

#using the or operator to determine if either integer is less than 100
if num1<100 or num2<100:
    print('Either number is less than 100: True\n')
else:
    print('Either number is less than 100: False\n')

#using not operator to determine of num1 is equal to num2

if not num1==num2:
    print('num1 is not equal to num2: True\n')
else:
    print('num1 is not equal to num2: False\n')
#using not operator to determine if either integer is equal to zero
if not num1>0:
    print('num 1 is not 0: False\n')
else:
    print('num 1 is not 0: True\n')