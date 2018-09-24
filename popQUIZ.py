
"""import random

x=random.randint(-5,5)
print(x)"""

"""for i in range(500):
    y=8
    print(y)"""
acc = 0
for i in range(1000):
    x=int(input("give me an intger so i can look at it: "))
    
    if (x%2 == 0):
        print("your number, " + str(x)+ ", is even")
        acc +=1 #this is the same thing as acc = acc + 1
    elif (x%2==1):
        print("your number, " + str(x)+ ", is odd")
print("numder og evens is" + str(acc))
print("number of odds is" + str(acc))





