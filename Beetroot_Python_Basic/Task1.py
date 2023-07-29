#Write a program that generates a random number 
#between 1 and 10 and 
#lets the user guess what number was generated. 
#The result should be sent back to the user via a print statement.
import random
random_number=random.randint(1,10)
my_number=int(input("Please,enter your number:"))
if random_number==my_number:
    print("You win!")
else:
    print("Try again!")
print(f"My number was:  {random_number}")


