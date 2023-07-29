#Words combination
#Create a program that reads an input string and then creates and prints 5 random strings from characters of the input string.
#For example, the program obtained the word ‘hello’, so it should print 5 random strings(words) that combine characters 
import random
input_string=input("Please,enter your string: ")
input_list=list(input_string)
for words in range(5):
    random.shuffle(input_list) # changes the order of elements in the list
    print("".join(input_list)) # makes a string from list
