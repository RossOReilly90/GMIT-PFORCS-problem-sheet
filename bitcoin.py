# This program displays the current value of Bitcoin 
# Authour - Ross O'Reilly
# Date - 08/02/21
#
import requests

print ("\n-------------")
print ("Bitcoin Value")
print ("-------------\n")
url = "https://api.coindesk.com/v1/bpi/currentprice.json"
returnedData = requests.get(url)
bitCoinDict = returnedData.json()

#print ('"USD rate": $',bitCoinDict['bpi']['USD']['rate_float'])
#print ('"GBP rate": £',bitCoinDict['bpi']['GBP']['rate_float'])
#print ('"EUR rate": €',bitCoinDict['bpi']['EUR']['rate_float'])
usRate = (bitCoinDict['bpi']['USD']['rate_float'])
gbpRate = (bitCoinDict['bpi']['GBP']['rate_float'])
eurRate = (bitCoinDict['bpi']['EUR']['rate_float'])

print ("The rate of Bitcoin in US dollars is:   $", round(usRate, 2))
print ("The rate of Bitcoin in GB pounds is:    £", round(gbpRate, 2))
print ("The rate of Bitcoin in Euros is:        €", round(eurRate, 2))

print ("\n-------------")

# jsonlint.com was the biggest help for me as it displayed the json file
# in a clear readable way