#11/02/2023
#CIT-110 P3HW1 - Debugging
#Raul Gonzales
#



# This program takes a number grade , determines average and displays letter grade for average.

# Enter grades for six modules

print('Enter grade for Module 1: ', end= ' ')
mod_1 = float(input())
print('Enter grade for Module 2: ', end= ' ')
mod_2 = float(input())
print('Enter grade for Module 3: ', end= ' ')
mod_3 = float(input())
print('Enter grade for Module 4: ', end= ' ')
mod_4 = float(input())
print('Enter grade for Module 5: ', end= ' ')
mod_5 = float(input())
print('Enter grade for Module 6: ', end= ' ')
mod_6 = float(input())


# add grades entered to a list
grades = (mod_1, mod_2, mod_3, mod_4, mod_5, mod_6)


#Declaring variables for low, high, sum and average
low = min(grades)
high = max(grades)
sum_grades = sum(grades)
avg = sum(grades) / len(grades)

#Print Results
print('------------Results------------')
print('Lowest Grade:     ', low)
print('Highest Grade:    ', high)
print('Sum of Grades:    ', sum_grades)
print(f'Average:           {avg:.2f}')
print('-------------------------------')

# determine letter grade for average
if avg >= 90:
 print('Your grade is: A')

elif avg >= 80:
 print('Your grade is: B')

elif avg >= 70:
 print('Your grade is: C')

elif avg >= 60:
 print('Your grade is: D')
 

else:
 print('Your grade is: F') 





