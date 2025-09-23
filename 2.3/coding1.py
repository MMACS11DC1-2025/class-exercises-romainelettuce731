"""
Write an Age in 2049 program that asks your age and outputs how old you'll be 31 years from now.

Examples:

How old are you?
> 10
In 2056, you will be 41 years old!
--
How old are you?
> 25
In 2056, you will be 56 years old!
"""
print("Hello! I will determine your age in 2049. Please input your age.")
age = int(input())
oldage = str(age+31)
print("In 2049, you will be "+oldage+" years old!")
