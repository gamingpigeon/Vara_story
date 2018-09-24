#WRITE A PROGRAM THAT WILL ASK THE USER WHAT THEIR AGE IS AND THEN DETERMINE IF THEY ARE OLD ENOUGH TO VOTE AND RESPOND APPROPIATELY

ask=int(input("how old are you?:"))

if ask <int(18):
    
    print("you can't vote :'(")
    
elif ask >= int(18):
    
     print("you can vote :)")