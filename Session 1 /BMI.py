# This program asks the user for their weight in pounds and their height in feet and inches, and calculates/displays their BMI to one decimal place(as defined by the World Health Organization).

# Gather user data
weight = int(input('What is your weight in pounds?\n'))
feet = int(input('What is your height in feet and inches?\n'))
inches = int(input())

# Calculate Height/BMI
height = (feet 
        * 12 
        + inches)
bmi = round(703 
            * weight 
            / 
            height**2, 1)

# Display BMI/legend
print("Your BMI is", bmi)
print("According to the World Health Organization, a BMI less than 18.5 is underweight, and a BMI greater than or equal to 25 is overweight")
