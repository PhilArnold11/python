#global variables
POUND = 0.453592 KILOGRAMS
INCH = 0.0254 METERS
def main():
    entered_weight = float(input)("Enter your wieght in pounds:  ")
    weight=entered_weight * POUND
    entered_height = float(input)("Enter your hieght in inches:  ")
    height=entered_height * INCH

    bmi = weight / height * height
    print(f'Your BMI is {bmi: .2f}')
    if bmi < 18.5:
        print('You are in the underweight category.')
    elif bmi <= 24.9:
        print('You are in the normal weight category.')
    elif bmi <= 29.9:
        print('You are in the overweight category.')
    else:
        print('You are in the obese category.')
main()
