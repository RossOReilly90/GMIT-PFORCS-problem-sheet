# Bitcoin Rates
#
# This program will display the current (hourly) rate of bitcoin in 3 currencies (USD,GBP,EUR) 
# A get request is made via url of a json file. 
# The data is converted to python dictionary then the rates are displayed to the user 
#
# Authour - Ross O'Reilly
# Date - 08/02/21

# REFERENCES
# Andrew Beatty - Lecturer notes. Lines (22-24)
# https://jsonlint.com - Helped me to see how JSON files are designed
# https://www.w3schools.com/python/python_json.asp - Reserched JSON a bit more 


import requests                                             # Imports requests mdule. Allows http requests to be sent in python

print ("\n-------------")                                   # Program banner
print ("Bitcoin Value")
print ("-------------\n")
                                                            
url = "https://api.coindesk.com/v1/bpi/currentprice.json"   # URL of a JSON file that updates bitcoin values hourly was set as 'url'
returnedData = requests.get(url)                            # The request for this json was made and stored in a variable called returnedData
bitCoinDict = returnedData.json()                           # The json data was the converted into bitCoinDict
 
usRate = (bitCoinDict['bpi']['USD']['rate_float'])          # Stores the float rate into each of the associated variables
gbpRate = (bitCoinDict['bpi']['GBP']['rate_float'])         # I done this because it allows me to round these floats to 2 decimal places
eurRate = (bitCoinDict['bpi']['EUR']['rate_float'])         # Whereas the 'rate' was a string and therefore couldn't be rounded

print ("The rate of Bitcoin in US dollars is:   $", round(usRate, 2))   # Displays message and value of bitcoin in 3 different currencies
print ("The rate of Bitcoin in GB pounds is:    £", round(gbpRate, 2))  # rounded to 2 decimal places
print ("The rate of Bitcoin in Euros is:        €", round(eurRate, 2))  # Euro symbol - copied the text into a word doc. Inserted € symbol then copied back here


print ("\n-------------")                                   # Border for visual effect

# NOTES
# jsonlint.com was the biggest help for me as it displayed the json file in a clean manner which i could then use to extract the information i needed
# This is the code i used to display the currency rates before i decided to create 3 variables and round up the rates
# print ('"USD rate": $',bitCoinDict['bpi']['USD']['rate_float'])
# print ('"GBP rate": £',bitCoinDict['bpi']['GBP']['rate_float'])
# print ('"EUR rate": €',bitCoinDict['bpi']['EUR']['rate_float'])