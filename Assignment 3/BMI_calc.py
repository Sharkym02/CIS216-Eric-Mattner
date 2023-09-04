# This program asks the user which units to use for calculating their BMI, takes their height and weight as input, and calculates/displays their BMI to one decimal place(as defined by the World Health Organization).

from BMI import BMI

# Initialize object for user
person = BMI()

# Ask user which units to use
while True:
        try:
                units = int(input('Enter "1" if you would like to use metric units, enter "2" if you would like to use imperial\n'))
                if units == 1 or units == 2:
                        break
                print("Please type 1 or 2")
        except:
                print("Please type 1 or 2")
        


# Determine which units to use and calculate BMI
if units == 1:
        person.kilograms = float(input('What is your weight in kilograms?\n'))
        person.meters = float(input('What is your height in meters?\n'))
        
elif units == 2:
        person.pounds = float(input('What is your weight in pounds?\n'))
        person.feet = float(input('What is your height in feet and inches?\n'))
        person.inches = float(input())

# Display BMI/legend
print("Your BMI is", person.bmi)
print("According to the World Health Organization, a BMI less than 18.5 is underweight, and a BMI greater than or equal to 25 is overweight")
