# Body mass index calculator
# 
# This program will take in the users weight and height
# and calculate the individuals BMI
# Error catching is included to prevent invalid inputs for weight and height
#
# Author - Ross O'Reilly
# Date - 30/01/21

# REFERENCES
# https://www.w3resource.com/python-exercises/python-basic-exercise-66.php
# https://www.youtube.com/watch?v=KdMAj8Et4xk - Examples of error catching using try and execute 



print("\n\n====================================")                   # Program banner  
print ("Body Mass Index\n\nPlease enter your details.")         
print("====================================")                   

StayInLoop = True                                                   # Boolean variable to help with looping
while StayInLoop == True:                                           # Beginning of weight loop - while StayInLoop is true
    try:                                                            # Error correction - if input type is correct (in this case a float) 
        weight = float(input("Enter your weight in Kilograms: "))   # Takes in user weight input and checks that is it a float. If it's not, program will go straight to 'except'
        if 0< weight <600:                                          # If the input is a float and is between 0 and 600 kgs
            StayInLoop = False                                      # Boolean is now false and therefore the while loop will break
        else:                                                       # If the float value is outside of the weight range i set (0< - 600)
            print("Please enter a realistic weight. ")              # An error message will display asking for a realistic value 
            StayInLoop = True                                       # The boolean will stay true so the while loop begins again
    except:                                                         # Error correction - if input type is wrong (not a float)
        print("Please enter a numeric weight. ")                    # Error message displayed asking for a numeric value to be entered
        continue                                                    # Used to end the current iteration in a loop - in this case restarts the while loop

StayInLoop = True                                                               # Reset the boolean variable as it will be used again in same methid for height input
while StayInLoop == True:                                                       # Beggining of height loop - while StayInLoop is true 
    try:                                                                        # Error correction - if input type is correct (in this case a float)
        heightCm = float(input("Please enter your weight in centimeters:"))     # Takes in user height input and checks that it is a float. If it's not, program will go straight to 'except'  
        if 30.48 <= heightCm <= 304.8:                                          # If the input is less than 30.48cm (1ft) or more than 304.8cm (10ft)
            StayInLoop = False                                                  # Boolean is now false and therefore the while loop will break
        else:                                                                   # If the float value is outside of the height range mentioned 2 ines up
            print("Please enter a valid height.")                               # An error message will be displayed asking for a valid height
            StayInLoop = True                                                   # The boolean will stay true so the while loop begins again
    except:                                                                     # Error correction - if the input type is wrong (not a float)
        print("Please enter a numeric height. ")                                # Error message displayed asking for a numeric value to be entered
        continue                                                                # Used to end the current iteration in a loop - this while loop

height = heightCm / 100                                         # Converts cm to m by dividing by 100
bmi = weight / (height*height)                                  # BMI formula is calculated and stored in the 'bmi' variable

print ("\nYour body mass index is:\t ", round(bmi,2))           # Displays message and the prints bmi value rounded to 2 decimal places
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
print ("\nThank you!\n")


# NOTES
# Found a site for a good example of how to display text and get an input in one short line (lines 11 and 12) referenced above
# Used the c++ syntax && for the conditions (wouldn't work). Python has a great shorthand way of doing this by putting the variables between two numbers
# If required, could use reg ex to prevent user from crashing program by inputting text instead of numbers
# Tried this but didn't find it to be great in this situation
# Looked up youtube and found a good video on how to get the type of input you want by doing error correction