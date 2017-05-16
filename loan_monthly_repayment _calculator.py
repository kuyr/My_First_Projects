#loan monthly repayment calculator
#declare and initialize the variables

monthlyPayment = 0
loanAmount = 0
interestRate = 0
numberOfPayments = 0
loanDurationInYears = 0

#request for the user to enter their data

loanAmountStr = input('please enter the amount you wish to loan\n')
interestRateStr = input('please enter the interest rate in percentage\n')
loanDurationInYearsStr = input('please enter how long it would take you to pay back in years\n')

#convert the strings to floats

loanAmount = float(loanAmountStr)
interestRateInPercent = float(interestRateStr)
loanDurationInYears = float(loanDurationInYearsStr)

interestRate = interestRateInPercent / 100
totalPay = loanAmount + (loanAmount * interestRate)

#convert duration of payments to number of
numberOfPayments = loanDurationInYears * 12

#calculate monthly repayment

monthlyPayment = totalPay / numberOfPayments

print(monthlyPayment)
print('you would be needed to pay NGN%0.2f monthly' % (monthlyPayment))



