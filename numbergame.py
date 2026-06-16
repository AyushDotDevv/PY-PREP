#guessingGame 
import random 
a=random.randint(1,100)
print (a)
x=0
while True :
    b=int(input ("enter your guess"))
    if x<5:
        if b<a:
            print ("too low , try again !!")
            x=x+1
        elif b>a:
            print("too high , try again !!")
            x=x+1
        else :
            print ("you gussed it right")
            x=x+1
            break
    else:
        print ("out of attempts")  
        break  
print(f"number of attempts are {x}")