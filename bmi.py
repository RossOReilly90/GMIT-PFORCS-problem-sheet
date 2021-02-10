# This is a body mass index calculator
# Author - Ross O'Reilly
# Date - 30/01/21

# References
# https://www.w3resource.com/python-exercises/python-basic-exercise-66.php

print("\n\n====================================")   	        # Added for visual effect
print ("Body Mass Index\n\nPlease enter your details.")         # Prints the title of the program
print("====================================")                   # Added for visual effect
weight = float(input("Enter your weight in Kilograms:\t "))     # Prompts the user to enter weight and then stores the float value in the 'weight' variable
height = float(input("Enter your height in Meters: \t "))       # Prompts the user to enter height and then stores the float value in the 'height' variable
bmi = weight / (height*height)                                  # BMI formula is calculated and stored in the 'bmi' variable

print ("\nYour body mass index is:\t", round(bmi,2))            # Displays message and the prints bmi value rounded to 2 decimal places
if 0 <= bmi <= 18.99:                                           # If statement with 5 conditions
    print("You are Underweight")                                # If bmi is less than 19 a message will display saying underweight
elif 19.0 <= bmi <= 23.99:
    print ("You are Healthy")                                   # If bmi is between 19 and 23.99 a message will display saying healthy 
elif 24.0 <= bmi <= 29.99 :
    print ("You are Overweight")                                # If bmi is between 24 and 29.99 a message will display saying overweight
elif 30.0 <= bmi <= 39.99:
    print ("You are Obese")                                     # If bmi is between 30 and 39.99 a message will display saying obese
else:                                                           
    print ("You are Extremely Overweight")                      # If bmi is over 40 a message will display saying extermely obese
print("====================================")
print ("\nThank you!\n\n")


# NOTES
#
# Found a site for a good example of how to display text and get an input in one short line (lines 11 and 12) referenced above
# Used the c++ syntax && for the conditions (wouldn't work). Python has a great shorthand way of doing this by putting the variables between two numbers