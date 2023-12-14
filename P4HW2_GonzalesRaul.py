#CTI-110
#P4HW2 - Salary Calculator
#Raul Gonzales
#11/28/2023
#

#Lists needed for final summary
total_overtime = []
total_reg_hrs = []
total_gross = []

#Employee counter
i = 0
               
employee_name = input("Enter employee's name or 'Done' to terminate: ")

while employee_name != "Done":
    hrs_work = float(input(f'How many hours did {employee_name} work? '))
    pay_rate = float(input(f"What is {employee_name}'s pay rate? "))
  
    if hrs_work > 40:
        overtime = hrs_work - 40.00
        reg_pay = 40.00 * pay_rate
        overtime_pay = pay_rate * overtime * 1.5
        gross_pay = reg_pay + overtime_pay
    else:
        overtime = 0.00
        reg_pay = pay_rate * hrs_work
        overtime_pay = 0.00
        gross_pay = reg_pay
        
    print()
    print('Employee name:', employee_name)
    print()
    print('Hours Worked   Pay Rate       OverTime       OverTime Pay   RegHour Pay    Gross Pay')
    print('--------------------------------------------------------------------------------------')
    print(f'{hrs_work:<17.1f}{pay_rate:<16.2f}{overtime:<15.1f}${overtime_pay:<12.2f}${reg_pay:<12.2f}${gross_pay:<13.2f}\n')
    
    total_overtime.append(overtime_pay)
    total_reg_hrs.append(reg_pay)
    total_gross.append(gross_pay)

    i += 1

    employee_name = input("Enter employee's name or 'Done' to terminate: ")
    
print()
print(f'Total number of employees entered: {i}')
print(f'Total amount paid for overtime: ${sum(total_overtime):.2f}')
print(f'Total amount paid for regular hours: ${sum(total_reg_hrs):.2f}')
print(f'Total amount paid in gross: ${sum(total_gross):.2f}')
                        
        
  
