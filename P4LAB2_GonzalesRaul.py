#Get two inputs from user
num1 = int(input())
num2 = int(input())

#Start of loop
if num1 <= num2:
    while num1 <= num2:
        print(num1, end= ' ')
        num1 += 5
else:
    print("Second integer can't be less than the first.",end='')

# Print an empty line at the end
print()

