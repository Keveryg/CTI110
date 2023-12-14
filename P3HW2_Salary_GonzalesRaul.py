#CTI-110
#P3HW2 - Salary
#Raul Gonzales
#11-3-2023
#


#Ask for employees name, total hours worked and pay rate
print("Enter employee's name:", end=' ')
employee_name = str(input())
print('Enter number of hours worked:', end=' ')
hrs_worked = float(input())
print("Enter employee's pay rate:", end=' ')
pay_rate = float(input())

#Use variables to establish Overtime pay and regular pay with If statement
if hrs_worked > 40:
    regular_pay = pay_rate * 40.00
    overtime_pay = (hrs_worked - 40.00) * (pay_rate * 1.5)
    overtime = hrs_worked - 40.00

else:
    regular_pay = pay_rate * hrs_worked
    overtime_pay = 0
    overtime = 0

#Establish gross pay variable
gross_pay = regular_pay + overtime_pay

#Add two decimal points to regular pay + gross pay
regular_pay = f'{regular_pay:.2f}'
gross_pay = f'{gross_pay:.2f}'

#Adding $ sign to currency variables
regular_pay = '$' + str(regular_pay)
gross_pay = '$' + str(gross_pay)

#Configure format for report generated
print('-------------------------------------')
print('Employee name: ', employee_name)
print()
print('Hours Worked   ', 'Pay Rate        ', 'OverTime       ', 'RegHour Pay    ', 'Gross Pay      ')
print('--------------------------------------------------------------------------------')
print(f'{hrs_worked:<17.1f}{pay_rate:<17.1f}{overtime:<17.1f}', regular_pay,'    ', gross_pay)
