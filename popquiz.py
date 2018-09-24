import time

ask = int(input("give me a whole number and i will count down from it: "))

for i in range(ask + 1):
    print(ask)
    ask = ask - 1
    time.sleep(1)
    #i did it :)

