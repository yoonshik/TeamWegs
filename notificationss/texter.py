# Reading in data from to_numbers.txt
# Need format: "name xxx-xxx-xxxx" "name (xxx) xxx-xxxx" "name xxxxxxxxxx"
import re
from twilio.rest import TwilioRestClient 

# put your own credentials here 
ACCOUNT_SID = "AC2a33a12da8051b42d3eebabb52c6c6b1" 
AUTH_TOKEN = "4d60e9793b228759f6d3265537d02c12" 

client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 

file = open ('to_numbers.txt', 'r')
count = 1
for line in file:
	tuples = re.findall(r'([a-zA-Z ]+)\s+([-0-9() ]*)', line)
	tuples = tuples[0]

	if tuples:
		name = tuples[0]
		number = tuples[1]
		print count, name, number
		count=count+1
		client.messages.create( 
			to_=number,
			from_="+13012501522",
			body= "Hi " + name + ",  there is currently free food in the kitchen at the Germantown office. Enjoy! -Team Wegs"
		)
file.close()