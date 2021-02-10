# This program displays the current value of Bitcoin 
# Authour - Ross O'Reilly
# Date - 08/02/21

# REFERENCES
# Andrew Beatty - Lecturer notes
# https://jsonlint.com - Helped me to see how JSON files are designed
# https://www.w3schools.com/python/python_json.asp - Reserched JSON a bit more 


# Allows http requests to be sent in python
import requests

# Displays program heading
print ("\n-------------")
print ("Bitcoin Value")
print ("-------------\n")
 
# These lines of code were provided by lecturer Andrew Beatty
# URL of a JSON file that updates bitcoin values hourly was set as 'url'
# The request for this json was made and stored in a variable called returnedData
# The json data was the converted into bitCoinDict
url = "https://api.coindesk.com/v1/bpi/currentprice.json"
returnedData = requests.get(url)
bitCoinDict = returnedData.json()
# print("bitCoinDict") - i deleted this after copied the data to jsonlint.com and 
# figured out how to access the specific labels


# This is the code i used to display the currency rates 
# before i decided to create 3 variables and round up the rates
#print ('"USD rate": $',bitCoinDict['bpi']['USD']['rate_float'])
#print ('"GBP rate": £',bitCoinDict['bpi']['GBP']['rate_float'])
#print ('"EUR rate": €',bitCoinDict['bpi']['EUR']['rate_float'])

# Stores the float rate into each of the associated variables
# I done this because it allows me to round these floats to 2 decimal places
# Whereas the 'rate' was a string and therefore couldn't be rounded 
usRate = (bitCoinDict['bpi']['USD']['rate_float'])
gbpRate = (bitCoinDict['bpi']['GBP']['rate_float'])
eurRate = (bitCoinDict['bpi']['EUR']['rate_float'])

# Displays message and value of bitcoin in 3 different currencies 
# rounded to 2 decimal places
print ("The rate of Bitcoin in US dollars is:   $", round(usRate, 2))
print ("The rate of Bitcoin in GB pounds is:    £", round(gbpRate, 2))
print ("The rate of Bitcoin in Euros is:        €", round(eurRate, 2))

# Border for visual effect
print ("\n-------------")

# NOTES
# jsonlint.com was the biggest help for me as it displayed the json file in a clean manner
# which i could then use to extract the information i needed