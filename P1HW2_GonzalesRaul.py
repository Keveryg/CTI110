#This project will use the users input to calculate travel expenses
#10/19/2023
#CTI-110 P2HW1 - Travel
#Raul Gonzales
#
print('This program calculates and displays travel expenses')
print()
print('Enter Budget:', end=' ')
budget = float(input())
print()
print('Enter your travel destination:', end=' ')
destination = input()
print()
print('How much do you think you will spend on gas?', end=' ')
gas = float(input())
print()
print('Approximately, how much will you need for accomadation/hotel?', end=' ')
accomodation = float(input())
print()
print('Last, how much do you need for food?', end= ' ')
food = float(input())
print()

expenses = gas + accomodation + food

#Turns float input into a string so that input can be combined w/"$" while keeping float input variables
budgetTE = "$" + str(budget)
gasTE = "$" + str(gas)
accomodationTE = "$" + str(accomodation)
foodTE = "$" + str(food)
Remaining_Balance = "$" + str(budget - expenses)

print('------------Travel Expenses------------')
print('Location:           ',destination)
print('Initial Budget:     ',budgetTE)
print('Fuel:               ',gasTE)
print('Accomodation:       ',accomodationTE)
print('Food:               ',foodTE)
print('---------------------------------------')
print()
print('Remaining Balance:  ', Remaining_Balance)


#Program takes the users input to help keep track of travel expenses.
#The fuel, accomodation, and food costs are deducted from the overall Initial Budget.
#There are two variables for each expense one to display the input as a float
#The next enables the inputs to be combined with a special character ("$") as a string.








