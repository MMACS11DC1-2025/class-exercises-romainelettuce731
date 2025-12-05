"""
Write an Olympic Judging program that outputs the average scores from 5 different judges. 

Each score is out of 10 points maximum. Half points are allowed (e.g. 7.5)

The program should take 5 inputs and output the final average score.

Example:

Judge 1: 5.5
Judge 2: 10
Judge 3: 7
Judge 4: 8.5
Judge 5: 9
Your Olympic score is 8.0
"""

print("Hello! Please input 5 scores and I will output the average. You can enter whole numbers between 1 ")
print("and 10 as well as any of those numbers + .5")
score = 0

score += float(input())
score += float(input())
score += float(input())
score += float(input())
score += float(input())

score = score/5
print("Your average score is "+str(score))
