from datetime import datetime
while True:
	try:
		bDay = input("Please enter your date of birth (eg. October 29 1988):")
		birthDay = datetime.datetime.strptime(bDay, '%B %d %Y')
		break
	except ValueError:
		print("Your birthdate cannot be processed. Please put in format 'Month Day Year' without a leading space.")
	
tDay = datetime.datetime.today()
timedelta = (tDay - birthDay).total_seconds()
print("You have existed for:",timedelta,"seconds")