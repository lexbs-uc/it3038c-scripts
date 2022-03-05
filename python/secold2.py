import datetime
while True:
    try:
        b_Day = input("Please enter your exact Date of Birth(eg. October 29 1988):")
        birthDay = datetime.datetime.strptime(b_Day, '%B %d %Y')
        break
    except:
        print("Please put in the Format 'Month Day Year' without any initial space")

t_Day = datetime.datetime.today()
timeGamma = (t_Day - birthDay).total_seconds()
print("You have lived for:",timeGamma,"seconds")

print("Converted into days, hours, minutes, and with seconds remaining, you have lived...")
secs = timeGamma
result = datetime.timedelta(seconds = secs)
print("\n", result, "\n")