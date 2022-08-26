# This is where functions from the user programmed module are implemented to ensure that there is minimal hassle in the main executed code.

from functions import *

while True:
    
    cmd = input("\n  What do you want to do? (enter number only) \n   0: Exit \n   1: Encode \n   2: Decode \n   3: Change encryption key \n\n  ")

    if cmd == "0":
        break
    
    elif cmd == "1":
        # The function that encodes files.
        encode(input("\n  Enter file path: "))
        
    elif cmd == "2":
        # The function that decodes files.
        decode(input("\n  Enter file path: "))
        
    elif cmd == "3":
        # The function that changes the key.
        setKey()
    
    else:
        print("\n  Enter a vaild command.")