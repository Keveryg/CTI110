#This program creates a math quiz for the user
#12/12/2023
#CTI-110 P5HW - Math Quiz
#Raul Gonzales
#

import random

num1 = random.randint(1, 100)
num2 = random.randint(1, 100)
answer = 0
selection = 0

def addition(num1, num2):
    answer = num1 + num2
    return answer
def subtraction(num1, num2):
    answer = num1 - num2
    return answer

def main_menu():
    print('Welcome to Math Quiz\n\n')
    print('MAIN MENU')
    print('---------------------')
    print('1. Adding Random Numbers\n2. Subtracting Random Numbers\n3. Exit\n')
    selection = int(input('Please choose one of the menu options: '))
    return selection

while selection != 3:
    selection = main_menu()

    if selection == 1:
        guesses = 0
        print(f'  {num1}\n+ {num2}')
        while answer != addition(num1, num2):
            answer = int(input('Enter answer.\n'))
            if answer > addition(num1, num2):
                guesses += 1
                print('Sorry, guess is too high.')
            elif answer < addition(num1, num2):
                guesses += 1
                print('Sorry, guess is too low.')
            elif answer == addition(num1, num2):
                guesses += 1
                print('Congratulations!!!! Your answer is correct.')
                print(f'Number of guesses: {guesses}')
    elif selection == 2:
        guesses = 0
        print(f'  {num1}\n- {num2}')
        while answer != subtraction(num1, num2):
            answer = int(input('Enter answer.\n'))
            if answer > subtraction(num1, num2):
                guesses += 1
                print('Sorry, guess is too high.')
            elif answer < subtraction(num1, num2):
                guesses += 1
                print('Sorry, guess is too low.')
            elif answer == subtraction(num1, num2):
                guesses += 1
                print('Congratulations!!!! Your answer is correct.')
                print(f'Number of guesses: {guesses}')
    elif selection == 3:
        print('Thank you for playing...')
    else:
        print("You have entered invalid selection. Please try again.")

print('Bye!!')
            
        
