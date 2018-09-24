import random

def EvenOdd():#funtionName or anything expext what i already used
    acc = 0
    for i in range(1000):
        x=int(input("give me an intger so i can look at it: "))
        
        if (x%2 == 0):
            print("your number, " + str(x)+ ", is even")
            acc +=1 #this is the same thing as acc = acc + 1
        elif (x%2==1):
            print("your number, " + str(x)+ ", is odd")
    print("numder of evens is" + str(acc))
    print("number of odds is" + str(acc))
    
def greeting():
    print("what is your name: ")
    print("that is cool")

def ask():
    ask=int(input("how old are you?:"))

if ask <int(18):
    return ask
    print("you can't vote :'(")
    
elif ask >= int(18):
    
    print("you can vote :)")