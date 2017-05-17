charges = 0
extraCharges = 0
charges = input('please enter the amount of your total purchase')
extraCharges = float(charges) + 10

if float(charges) >= 50:
    print('you get free shipping')
    print('your final total is NGN' + str(charges))


else:
    print('you would have to pay ' + str(extraCharges))
    print('your total is NGN' + str(extraCharges))





