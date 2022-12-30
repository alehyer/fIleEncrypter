# This is where functions from the user programmed module are implemented to ensure that there is minimal hassle in the main executed code.

from functions import *
import functions


while True:
    
    cmd = input("\n  What do you want to do? (enter number only) \n   0: Exit \n   1: Encrypt \n   2: Decrypt\n\n  ")

    if cmd == "0":
        break
    
    elif cmd == "1":
        # The function that encrypts files.
        encrypt(input("\n  Enter file path: "))
        setKey()
        
    elif cmd == "2":
        # The function that decrypts files.
        decrypt(input("\n  Enter file path: "))
        setKey()
    
    else:
        print("\n  Enter a vaild command.")