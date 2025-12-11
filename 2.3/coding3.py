"""
Write a McDoland's program that takes your order and outputs the total cost.

It first asks if you want a burger for $5. It then asks if you want fries for $3. It outputs the total with 14% tax.

The program should accept Yes/No or yes/no.

Example:

Would you like a burger for $5? (Yes/No)
> yes
Would you like fries for $3? (Yes/No)
> yes
Your total is $9.12

Would you like a burger for $5? (Yes/No)
> yes
Would you like fries for $3? (Yes/No)
> no
Your total is $5.699999999999999

Would you like a burger for $5? (Yes/No)
> no
Would you like fries for $3? (Yes/No)
> yes
Your total is $3.42
"""
money = 0

print("Hello, welcome to McDolands. May I take your order?")
print("Would you like a burger for $5? (Yes/No)")
burg = input().lower()
print("Would you like fries for $3? (Yes/No)")
fry = input().lower()

if burg == "yes":
    money += 5

if fry == "yes":
    money += 3

money = money*1.14
print("Your total is $"+str(money)+".")