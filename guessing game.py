import random
n=random.randint(0,20)
s=True
max=100
c=0
while s==True:
    print("Enter the guess number:")
    num=int(input())
    if num==n:
        c+=1
        print("               WONDERFULL!              ")
        if c==1:
            print(" THAT WAS QUICK YOU CLEARED IT YOUR FIRST ATTEMPT ")
            print("YOU SCORED :",max)
        else:
            print("               THAT's GREAT    ")
            print("  YOU GUESS THE NUMBER IN YOUR ", c, "ATTEMPTS    ")
            print("               YOU SCORED :",max+50)
        s=False
    else:
        print("OOPS !")
        print("SAND IS MORE USEFUL THAN YOUR BRAIN, TRY AGAIN")
        c+=1
        max-=50
        if n % 2 == 0:
            print("THE NUMBER IS EVEN ")
        else:
            print("THE NUMBER IS ODD")
if max<-100:
    print("your brain needs a neural repair in maths")
elif max==100:
    print("you nailed it ")
