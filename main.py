import random
x=int(input("Length of the password:"))
a="abcdefghijklmnopqrstuvwxyz"
b="1234567890"
print("".join(random.sample(a+b,36)))
