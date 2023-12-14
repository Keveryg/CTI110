#CTI-110
#P2WH2 - List
#Raul Gonzales
#10/24/2023
#


#Program will ask user for input of grades for Modules 1-6 and use inputs to assign values to variables. (Done)
#Values will then be stored in a list
#Each grade will be displayed as a float for each module
#List will be used to perform calculations for lowest grade, highest grade, sum of grades and grade average.
#Results will be right aligned and displayed as a float

print('The following program will be used to show details of your grades for Modules 1-6.')
print('Please enter your grade for Module 1:', end=' ')
Module_one = float(input())
print('Please enter your grade for Module 2:', end= ' ')
Module_two = float(input())
print('Please enter your grade for Module 3:', end= ' ')
Module_three = float(input())
print('Please enter your grade for Module 4:', end= ' ')
Module_four = float(input())
print('Please enter your grade for Module 5:', end= ' ')
Module_five = float(input())
print('Please enter your grade for Module 6:', end= ' ')
Module_six = float(input())


#Grades list
Grades = [Module_one, Module_two, Module_three, Module_four, Module_five, Module_six]
Grade_average = sum(Grades)/len(Grades)

#Displaying report starts here
print('------------Results------------')
print('Lowest Grade:        ',min(Grades))
print('Highest Grade:       ',max(Grades))
print('Sum of Grades:       ',sum(Grades))
print(f'Average:              {Grade_average:.2f}')
print('--------------------------------')

