import random
random_list=[]
i=0
while i<10:
    random_list.append(random.randint(1,100))
    i+=1
maxi=random_list[0]
j=0
while j<10:
    if (random_list[j]>maxi):
        maxi=random_list[j]
    j+=1
print(random_list)
print(maxi)
