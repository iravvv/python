#Make a program that checks if a string is in the right format for a phone number. 
#The program should check that the string contains only numerical characters and is only 10 characters long. 
#Print a suitable message depending on the outcome of the string evaluation.
Phone_number="80979282767"
if Phone_number.isdigit():
    #if len(Phone_number)==10:
    print("Format of Phone number is correct")
if len(Phone_number)==10:
    print("Numerical character of Phone number is correct")
else:
    print("Please check format and numerical characters of Phone number")