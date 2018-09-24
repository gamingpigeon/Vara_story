"""
write a program that willl take a number (intgers only) and return a statement 
that will let the user know if it is even or odd
"""
x=int(input("give me an intger so i can look at it: "))

if (x%2 == 0):
    print("your number, " + str(x)+ ", is even")
    
elif (x%2==1):
    print("your number, " + str(x)+ ", is odd")
    

    