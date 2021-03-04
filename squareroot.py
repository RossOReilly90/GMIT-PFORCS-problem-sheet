# Square root calculator
#
# This script will take in a positive float number and using newton method will calculate the square root
#
# Newton method - 
# root = 0.5 * (X + (N / X)) where X is any guess which can be assumed to be N or 1.
#
# Author - Ross O'Reilly
# Date - 01/03/21

# REFERENCES
# https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/#:~:text=Let%20N%20be%20any%20number,correct%20square%20root%20of%20N.- newton method formula
# https://medium.com/@sddkal/newton-square-root-method-in-python-270853e9185d
# https://docs.python.org/3/tutorial/inputoutput.html


while True:                                                     # While loop to get correct user input type
    try:                                                        # Error correction - If input type is correct
        num = float(input("Please enter a positive float: "))   # Takes input from user and checks if its an int. if not code will skip to 'except'
        if 0< num:                                              # If the interger is greater than 0 StayInLoop becomes false
            break                                               # This will then cause the while loop to break
        else:                                                   # If the input is 0 or less 
            print("Not a positive float")                       # An error message will ask for a positive interger
    except:                                                     # Error correction - If the input is not an int
        print("Invalid input")                                  # An error message will display invalid input   
        continue 

def sqrt(num):                                                  # User defined function. This function will calculate and return the square root of the enter number
    x = num                                                     # Stores the entered number in the variable x 
    while True:                                                 # Creates a loop which will continuously run the following equation
        root = 0.5 *(x + (num / x))                             # Newton method formula for square root calculation
        if (abs(root - x) <.01):                                # if the absolute (positive) difference between the current and previous number -
            break                                               # is less than a tolerance of .01 then break out of the loop
        x = root                                                # Sets x equal to the current root value for the next calculation
        continue                                                # Brings script back to the beginning of the while loop
    return root                                                 # The final value of root is returned and stored as num

print ("\n The square root of {} is approx: {:.2f}\n" .format (num, sqrt(num)))

# Nearly all of the material on newton method i found online was in realtion to an equation which wasn't relevant to this script
# I found a quicker and neater way of creating loops by using break instead of using variables
# I used 0.01 for the tolerance as i felt it was accurate enough for this script
# When formatting the num variable i struggled to get it the way i wanted. After a bit of research i found that all i needed to do was add 'f' after 2 in {:.2f}