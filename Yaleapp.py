# This is a comment
# print('There once was a movie star icon\n who preffered to sleep with the light on.\n They learned how to code\n a device that sure glowed\n and lit up at night using Python!')

# input from the user
# firstName = input('what is your first name?\n')
# secondName = input('enter your last name too\n')
# print('Hey '+ firstName +' '+ secondName )
#name = input('Hi, what is your name?\n')
#country = input('what country do you live in? \n')
#age = input ('how old are you?')
#country = country.upper()
#print('Hey my name is ' + name + ' ' +'and i am '+ age +' years old ' + 'and I love' + ' ' + country)

# working with maths
#area = 0
#height = 10
#width = 20

#calculating the area of a triangle

#area = width * height /2
#printing formatted float value with 0 decimal place
#print('the area of the triangle is %.0f' % area)
#print('here are three numbers! the first is {0:d} the second is {1:f} and {2:d}'.format(8,9,7))

#The import statement gives us access to the functionality of the datetime class

#Declare variables
orderTotal = 0
shippingCost = 0
totalWithShipping = 0

#Ask user for their order total and convert the answer to a number
orderTotal = float(input("What was the total for your order? " ))

#Calculate the shipping cost based on the order total
if orderTotal >= 50 :
    shippingCost = 0
else :
    shippingCost = 10

#Calculate order total including shipping
totalWithShipping = orderTotal + shippingCost

#Tell the user their final total
print("Your final total, including shipping, will be: $%.2f " % totalWithShipping)

























