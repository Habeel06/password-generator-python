import random
from termcolor import colored
import colorama 
colorama.init()



print(colored('''
      ___         ___                                  ___           ___           ___           ___           ___           ___                         ___           ___     
     /\  \       /\  \         _____                  /\__\         /\__\         /\  \         /\__\         /\  \         /\  \                       /\  \         /\  \    
    /::\  \     _\:\  \       /::\  \                /:/ _/_       /:/ _/_        \:\  \       /:/ _/_       /::\  \       /::\  \         ___         /::\  \       /::\  \   
   /:/\:\__\   /\ \:\  \     /:/\:\  \              /:/ /\  \     /:/ /\__\        \:\  \     /:/ /\__\     /:/\:\__\     /:/\:\  \       /\__\       /:/\:\  \     /:/\:\__\  
  /:/ /:/  /  _\:\ \:\  \   /:/  \:\__\            /:/ /::\  \   /:/ /:/ _/_   _____\:\  \   /:/ /:/ _/_   /:/ /:/  /    /:/ /::\  \     /:/  /      /:/  \:\  \   /:/ /:/  /  
 /:/_/:/  /  /\ \:\ \:\__\ /:/__/ \:|__|          /:/__\/\:\__\ /:/_/:/ /\__\ /::::::::\__\ /:/_/:/ /\__\ /:/_/:/__/___ /:/_/:/\:\__\   /:/__/      /:/__/ \:\__\ /:/_/:/__/___
 \:\/:/  /   \:\ \:\/:/  / \:\  \ /:/  /          \:\  \ /:/  / \:\/:/ /:/  / \:\~~\~~\/__/ \:\/:/ /:/  / \:\/:::::/  / \:\/:/  \/__/  /::\  \      \:\  \ /:/  / \:\/:::::/  /
  \::/__/     \:\ \::/  /   \:\  /:/  /            \:\  /:/  /   \::/_/:/  /   \:\  \        \::/_/:/  /   \::/~~/~~~~   \::/__/      /:/\:\  \      \:\  /:/  /   \::/~~/~~~~ 
   \:\  \      \:\/:/  /     \:\/:/  /              \:\/:/  /     \:\/:/  /     \:\  \        \:\/:/  /     \:\~~\        \:\  \      \/__\:\  \      \:\/:/  /     \:\~~\     
    \:\__\      \::/  /       \::/  /                \::/  /       \::/  /       \:\__\        \::/  /       \:\__\        \:\__\          \:\__\      \::/  /       \:\__\    
     \/__/       \/__/         \/__/                  \/__/         \/__/         \/__/         \/__/         \/__/         \/__/           \/__/       \/__/         \/__/    
''',"red"))

while True:

    x=input(colored("Length of the password (8-35 recommended). :","yellow"))
    try:
        y = int(x) 
        if y <= 35:
            
                        a="abcdefghijklmnopqrstuvwxyz"
                        b="1234567890"
                        c="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                        d="!@#$&+"
                        print(colored("Your generated password is : "+ "".join(random.sample(a+b+c+d,y)),"green"))
            

            
        else:
             print(colored("Try Again!The length should be less than or equal to 35.","blue"))
    except ValueError:
            print(colored("Length should be a whole number which should be between 8-35 (recommended). TRY AGAIN!","yellow"))
