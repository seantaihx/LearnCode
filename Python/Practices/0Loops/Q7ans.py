'''
Math Challenge (Assignment + Conditions)
Start with points = 0
Ask the user:
“What is 7 * 8?”
	•	If right, add 5 points (+=)
	•	If wrong, subtract 2 points (-=)
Print the final score.
'''

#Initialize the point to 0 first
points = 0

#Get user input for the answer and change the type into int
ans = int(input("What is 7 * 8: "))
if ans != 7*8:
    points -= 2
else:
    points += 5

print('Your final score is {}'.format(points))

'''SAMPLE OUTPUT
@seantaihx ➜ .../Practice/Python/Practices/0Loops (main) $ python Q7ans.py
What is 7 * 8: 56
Your final score is 5
@seantaihx ➜ .../Practice/Python/Practices/0Loops (main) $ 
'''