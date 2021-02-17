# Collatz
#
# This program will take a positive interger input from the user
# Error correction will prevent invalid inputs
# At each step, the next value is calculated by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one. 
# The process stops when the current value equals 1
# The values for each step are then displayed to the user
#
# Author - Ross O'Reilly
# Date - 10/02/21

StayInLoop = True                                               # Boolean to help with looping
while StayInLoop == True:                                       # While loop to get correct user input type
    try:                                                        # Error correction - If input type is correct
        num = int(input("Please enter a positive interger: "))  # Takes input from user and checks if its an int. if not code will skip to 'except'
        if 0< num:                                              # If the interger is greater than 0 StayInLoop becomes false
            StayInLoop = False                                  # This will then cause the while loop to break
        else:                                                   # If the input is 0 or less 
            print("Not a positive interger")                    # An error message will ask for a positive interger
            StayInLoop = True                                   # StayInLoop will stay true and the while loop will restart
    except:                                                     # Error correction - If the input is not an int
        print("Invalid input")                                  # An error message will display invalid input   
        continue                                                # The while loop will restart

original = num                          # The original input is stored in orginal. Used to display user input at the end. (start of display)
ans = [original,]                       # List used to store the user input and each value at every step. 

StayInLoop = True                       # Reset the variable for looping purposes                                  
while StayInLoop == True:               # Beginning of while loop for each step of the calculations
    if num == 1:                        # If the value equals 1 the calculations are over
        print(*ans, sep=', ')           # The entire list (ans) of numbers is printed to the user
        StayInLoop = False              # The while loop is broken and the program is finished
    elif num % 2 == 0:                  # If the number keeps dividing by 2 and has no remainder (aka if its even)
        num = num //2                   # Divide the current value by 2 (/ gives float value, // gives int value)
        ans.append(num)                 # Then add this number to the existing list of numbers
        StayInLoop = True               # The while loop restarts for the next calculation
    else:                               # IF the value isn't 1 or even, then its odd
        num = (num*3)+1                 # The new value is the current value multiplied by 3, then plus 1
        ans.append(num)                 # Add this current number to the list of existing numbers
        StayInLoop = True               # The while loop restarts for the next calculation