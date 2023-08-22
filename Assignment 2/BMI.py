# This program asks the user which units to use for calculating their BMI, takes their height and weight as input, and calculates/displays their BMI to one decimal place(as defined by the World Health Organization).

from bmi_calculator import bmi_calculator

# Ask user which units to use
units = int(input('Enter "1" if you would like to use metric units, enter "2" if you would like to use imperial\n'))

bmi = 0

# Determine which units to use and calculate BMI
if units == 1:
        user_input = bmi_calculator(float(input('What is your weight in kilograms?\n')), (float(input('What is your height in meters?\n'))))
        bmi = user_input.calculate_bmi_metric()
elif units == 2:
        user_input = bmi_calculator(float(input('What is your weight in pounds?\n')), (float(input('What is your height in feet and inches?\n')) * 12 + float(input())))
        bmi = user_input.calculate_bmi_imperial()


# Display BMI/legend
print("Your BMI is", bmi)
print("According to the World Health Organization, a BMI less than 18.5 is underweight, and a BMI greater than or equal to 25 is overweight")
