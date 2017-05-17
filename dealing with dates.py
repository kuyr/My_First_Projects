import datetime

#print(currentDate.month)
#print(currentDate.year)

#print(currentDate.strftime('%d %b, %Y'))
#print(currentDate.strftime('%d %b %y'))

#userInput = input('please enter your birthday let me tell you how many days you have lived for(dd/mm/yy) \n')
#birthday = datetime.datetime.strptime(userInput, '%d/%m/%Y').date()
#print(birthday)

#days = currentDate - birthday
#print(days.days)
totalDaysRem = 0
remWeeks = 0
remDays = 0
deadline = 0
strUserInput=''

currentDate = datetime.datetime.today()
strUserInput = input('please enter the deadline for your project dd/mm/yyyy:\n')
deadline = datetime.datetime.strptime(strUserInput, '%d/%m/%Y').date()

totalDaysRem = currentDate - deadline

print(totalDaysRem )