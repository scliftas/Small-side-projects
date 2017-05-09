#Caesar Cipher Encryption/Decryption Program
import time                                                               #Imports a time variable that can be used later on to pause the program.   
print("Welcome to this Caesar Cipher encryption and decryption program! ")#Welcomes the user to the program
time.sleep(1)                                                             #Pauses the script for a a second so as not to 'spam' the user with too much information at once
UserInput = input("Type E to encrypt or D to decrypt: ")                  #Asks the user if they want to encrypt or decrypt and stores their answer in the UserInput variable
if UserInput == ("E"):                                                    #Calls upon the UserInput variable, if they entered E it will run the encryption process
    UserInput2 = input("What do you want to encrypt? ")                   #Asks the user what they want to encrypt and stores their answer in the UserInput2 variable
    print(UserInput2)
    UserInput2 = [ord(i) for i in UserInput2]                             #Converts every character in the user's message into it's according ASCII Table value
    UserInput2 = [chr(i + 5) for i in UserInput2]                         #Converts every character back into the alphabet but shifts everything forwards by 5 characters
    UserInput2 = [word.replace('D','?') for word in UserInput2]           #Replaces what 'chr(i+5)' turns a question mark into
    UserInput2 = [word.replace('{','a') for word in UserInput2]           #Replaces what 'chr(i+5)' turns 'v' into, now looping around the alphabet instead
    UserInput2 = [word.replace('|','b') for word in UserInput2]           #Replaces what 'chr(i+5)' turns 'w' into, now looping around the alphabet instead
    UserInput2 = [word.replace('}','c') for word in UserInput2]           #Replaces what 'chr(i+5)' turns 'x' into, now looping around the alphabet instead
    UserInput2 = [word.replace('~','d') for word in UserInput2]           #Replaces what 'chr(i+5)' turns 'y' into, now looping around the alphabet instead
    UserInput2 = [word.replace('','e') for word in UserInput2]           #Replaces what 'chr(i+5)' turns 'z' into, now looping around the alphabet instead
    UserInput2 = [word.replace('%',' ') for word in UserInput2]           #Keeps spaces in the message
    UserInput2 = [word.replace('[','A') for word in UserInput2]           #Replaces what 'chr(i+5)' turns 'V' into, now looping around the alphabet instead
    UserInput2 = [word.replace('\\','B') for word in UserInput2]          #Replaces what 'chr(i+5)' turns 'W' into, now looping around the alphabet instead
    UserInput2 = [word.replace(']','C') for word in UserInput2]           #Replaces what 'chr(i+5)' turns 'X' into, now looping around the alphabet instead
    UserInput2 = [word.replace('^','D') for word in UserInput2]           #Replaces what 'chr(i+5)' turns 'Y' into, now looping around the alphabet instead
    UserInput2 = [word.replace('_','E') for word in UserInput2]           #Replaces what 'chr(i+5)' turns 'Z' into, now looping around the alphabet instead
    UserInput2 = [word.replace('&','!') for word in UserInput2]           #Replaces what 'chr(i+5)' turns an exclamation mark into
    print(UserInput2)
    UserInput2 = ''.join(UserInput2)                                      #Joins every character in the message into a string
    print("Your encrypted message is: ",UserInput2)                       #Tells the user what their encrypted message is
    time.sleep(30)
elif UserInput == ("D"):                                                  #Calls upon the UserInput variable and checks if they entered D instead of E
    UserInput2 = input("What do you want to decrypt? ")                   #Asks the user what they want to decrypt and stores their answer in the UserInput2 variable
    UserInput2 = [ord(i) for i in UserInput2]                             #Converts every character in the user's message into it's according ASCII Table value
    UserInput2 = [chr(i - 5) for i in UserInput2]                         #Converts every character back into the alphabet but shifts everything backwards by 5 characters
    UserInput2 = [word.replace('','!') for word in UserInput2]           #Replaces what 'chr(i - 5)' turns an exclamation mark into
    UserInput2 = [word.replace('\\','v') for word in UserInput2]          #Replaces what 'chr(i - 5)' turns 'a' into, now looping around the alphabet instead
    UserInput2 = [word.replace(']','w') for word in UserInput2]           #Replaces what 'chr(i - 5)' turns 'b' into, now looping around the alphabet instead
    UserInput2 = [word.replace('^','x') for word in UserInput2]           #Replaces what 'chr(i - 5)' turns 'c' into, now looping around the alphabet instead
    UserInput2 = [word.replace('_','y') for word in UserInput2]           #Replaces what 'chr(i - 5)' turns 'd' into, now looping around the alphabet instead
    UserInput2 = [word.replace('`','z') for word in UserInput2]           #Replaces what 'chr(i - 5)' turns 'e' into, now looping around the alphabet instead
    UserInput2 = [word.replace('',' ') for word in UserInput2]           #Keeps spaces in the message
    UserInput2 = [word.replace('<','V') for word in UserInput2]           #Replaces what 'chr(i - 5)' turns 'A' into, now looping around the alphabet instead
    UserInput2 = [word.replace('=','W') for word in UserInput2]           #Replaces what 'chr(i - 5)' turns 'B' into, now looping around the alphabet instead
    UserInput2 = [word.replace('>','X') for word in UserInput2]           #Replaces what 'chr(i - 5)' turns 'C' into, now looping around the alphabet instead
    UserInput2 = [word.replace('?','Y') for word in UserInput2]           #Replaces what 'chr(i - 5)' turns 'D' into, now looping around the alphabet instead
    UserInput2 = [word.replace('@','Z') for word in UserInput2]           #Replaces what 'chr(i - 5)' turns 'E' into, now looping around the alphabet instead
    UserInput2 = [word.replace(':','?') for word in UserInput2]           #Replaces what 'chr(i - 5)' turns a question mark into
    UserInput2 = ''.join(UserInput2)                                      #Joins every character in the message into a string
    print("Your decrypted message is: ",UserInput2)                       #Tells the user what their decrypted message is
    time.sleep(30)
else:                                                                     #Checks for any other input, all of which are invalid so it runs a process to close the program                                                          #Creates a while loop
    print("Invalid input. Closing program...")                            #Tells the user they have used an invalid input and that the program is closing down
    time.sleep(10)
                                                           

