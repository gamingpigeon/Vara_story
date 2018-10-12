"""this is all about functions"""

def greeting():
    print("hola")  
    
def Askname():
    name=input("what is your name: ")
    return name
def askage():
    age=int(input("what is your age: "))
    return age
def canvote(age):
    if (age >=18):
        print("you can vote:) ")
    else:
        print("you cannot vote :(")
    return canvote
#call the function
greeting()
x = Askname() #Save the output of Askname() to variable
print("hola " + x)
y = askage()
z = canvote(y)# z = if they can vote or note (T/F)
print(z)