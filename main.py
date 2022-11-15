import random
while True:
    x=int(input("Length of the password (it should be less than 35) :"))
    if x <= 35:
        a="abcdefghijklmnopqrstuvwxyz"
        b="1234567890"
        print("".join(random.sample(a+b,x)))

    else:
        print("Try Again-The length should be less than or equal to 35")
