#Write a Python program to get a string made of the first 2 and the last 2 chars from a given string.
#If the string length is less than 2, return instead of the empty string.
#string = "hello Earth"
#sub_string1 = string[0:2]
#sub_string2 = string[-2:]
#result=sub_string1+sub_string2
#print(result)
string = "h"
if len(string)>2:
    sub_string1 = string[0:2]
    sub_string2 = string[-2:]
    result=sub_string1+sub_string2
    print(result)    
elif len(string)<2:
    print(' ')
