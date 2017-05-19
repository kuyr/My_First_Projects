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
#team = input('enter your fav hockey team: ').upper()
#sport = input('enter your fav sport:  ').upper()
#import turtle

'''for steps in ['red','black','blue','brown']:
    turtle.color(steps)
    turtle.forward(100)
    turtle.right(90)
import turtle
shapeAngle = int(input('enter the angle to make:  '  ))
shapeSide = int(input('enter the length of the side of your shape:  '))
shapeColor = input('enter your fav color:  ')

while shapeSide !=0:
    turtle.color(shapeColor)
    turtle.forward(shapeSide)
    turtle.right(shapeAngle)

    if shapeSide != 0 :
        shapeColor = input("What pen color would you like to use? (black, blue, red, green): ")
        shapeAngle = int(input("What angle would you like? (0-360): "))

print("You are an amazing artist!")'''

'''for moving in range(shapeDraw):
       turtle.forward(shapeSide/2)
       turtle.right(360/shapeDraw)'''
guestsInput = ''
guestsList = []
nbrEntries = 0


guestsInput = input('Please enter tne name of guests attending the party:  ').upper()
nbrEntries = len(guestsList)

while guestsInput != 'DONE':
    guestsList.append(guestsInput)



    if guestsInput != 'DONE':
        guestsInput = input('Please enter tne name of guests attending the party:  ').upper()
        nbrEntries = len(guestsList)


guestsList.sort()
print(guestsList)

















'''print(guests)
guests[-1] = 'judas'
print(guests)
guests.append('mathew')
guests.remove('chris')
del guests[1]
print(guests)
print(guests[-1])'''




















