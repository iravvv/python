# Task 1

 def favorite_movie(name):
     return f"My favorite movie is named {name}"

 print(favorite_movie("Harry Potter"))

# Task 2

 def make_country(name,capital):
     dict_country={name:capital}
     return f"{capital} is the capital of {name}"
 print(make_country("Japan","Tokio"))

# Task 3
def make_operation(operator,*args):
    result=0
    if operator=="+":
        result=sum(args)
    elif operator == '-':
        result = args[0] - sum(args[1:])
    elif operator=="*":
        result=1
        for i in args:
            result*=i
    elif operator=="/":
        result=args[0]
        for i in args[1:]:
           result/=i
    else:
        return "Error"
    return result
print(make_operation(input("enter operator: "),2,6,5))