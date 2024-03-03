#global variables
POUND = 0.453592 
INCH = 0.0254
def main():
    entered_weight = float(input("Enter your wieght in pounds:  "))#input for weight
    weight=entered_weight * POUND #conversion to metric
    entered_height = float(input("Enter your hieght in inches:  "))#input for height
    height=entered_height * INCH #conversion to metric

    bmi = weight / (height * height)#BMI calculation
    print(f'Your BMI is {bmi: .2f}')#BMI displayed with two decimal places
#BMI Categories   
    if bmi < 18.5:
        print('You are in the underweight category.')
    elif bmi <= 24.9:
        print('You are in the normal weight category.')
    elif bmi <= 29.9:
        print('You are in the overweight category.')
    else:
        print('You are in the obese category.')
main()
