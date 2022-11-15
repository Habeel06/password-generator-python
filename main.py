import random

while True:

    x=input("Length of the password (it should be less than 35) :")
    
    try:
        y = int(x) 
        if y <= 35:
            
                        a="abcdefghijklmnopqrstuvwxyz"
                        b="1234567890"
                        c="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                        d="!@#$&+"
                        print("".join(random.sample(a+b+c+d,y)))
            

            
        else:
            print("Try Again-The length should be less than or equal to 35")
    except ValueError:
          print("Length should be a whole number which is between 8-35 (recommended). TRY AGAIN!")
