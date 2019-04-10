"""
Sams Teach Yourself Python in 24 Hours
by Katie Cunningham

Hour 4: Storing Text in Strings
Exercise:
1.
       a) You're given a string that contains the body of an email.
	   		If the email contains the word "emergency", print out
			"Do you wnat to make this email urgent?"
			If it contains the word "joke", print out 
			"Do you wnat to set this email as non-urgent?"

"""

#Hour 4: Storing Text in Strings
email_body = "This is an joke" #email type string
if 'Emeregency' in email_body:
	importance = raw_input("Do you want to set this email as urgent? YES or NO: ")
	if importance == "YES":
    		print ('Subject: Urgent! \n' + 'Message: ' + email_body.upper() + "!!!!!!!!!!!!") #urgent email
	elif importance == "NO":
        	print ('Subject: Non-Urgent \n' + 'Message: ' + email_body.lower() + "!!!!!!!!!!!!") #non-urgent email
	else:
		print ('Subject: Regular \n' + 'Message: ' + email_body) #regular email
elif 'joke' in email_body:
	importance = raw_input("Do you want to set this email as non-urgent? YES or NO: ")
	if importance == "YES":
    		print ('Subject: Joke \n' + 'Message: ' + email_body.lower()) #non-urgent email
	elif importance == "NO":
    		print ('Subject: Urgent \n' + 'Message: ' + email_body) #urgent email	
	else:
		print ('Subject: Regular \n' + 'Message: ' + email_body) #regular email