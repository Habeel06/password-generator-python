import random
x=int(input("Length of the password (it should be less than 35) :"))
a="abcdefghijklmnopqrstuvwxyz"
b="1234567890"
print("".join(random.sample(a+b,x)))
