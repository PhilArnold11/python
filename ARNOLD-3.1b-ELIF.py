score = float(input('Enter the numeric grade: '))

if score >=90:
    grade='A'
elif score >=80:
    grade='B'
elif score >=70:
    grade='C'
elif score >=60:
    grade='D'
elif score >=0:
    grade='F'
print('The letter grade is:', str(grade))