#CTI-110
#P4HW1 - Score List
#Raul Gonzales
#11-21-23
#

#Create loop variable
i = 1

# Ask user to enter number of scores
num_scores = int(input("How many scores do you want to enter? "))

#Create list for scores
scores = []

# Create a loop to collect the scores
#Determine if the score is between 0 and 100
while i <= num_scores:
    score = float(input(f'Enter score#{i}: '))
    if 0 <= score <= 100:
        scores.append(score)
        i = i + 1
    else:
        score = float(input(f"INVALID Score entered!!!!\nScore should be between 0 and 100\nEnter score #{i}: "))
        i = i + 1
     
        
# Calculate the lowest score
lowest_score = min(scores)

# Remove the lowest score from the list
scores.remove(lowest_score)

# Calculate the average of scores in modified list
average = sum(scores) / len(scores)

# Determine the letter grade for the calculated average and display it to user
if average >= 90:
    letter_grade = "A"

elif average >= 80:
    letter_grade = "B"

elif average >= 70:
    letter_grade = "C"

elif average >= 60:
    letter_grade = "D"

else:
    letter_grade = "F"

print()
print()
print('--------------Results-----------')
print('Lowest Score  : ', lowest_score)
print('Modified List : ', scores)
print(f'Scores Average: {average:.2f}')
print('Grade         : ', letter_grade)
print('--------------------------------')
    
    
