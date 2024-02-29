#global variables
1 POUND = 0.453592 KILOGRAMS
1 INCH = 0.0254 METERS
def main():
    weight = "Enter your weight in pounds:  "
    height = "Enter your height in inches:  "
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
