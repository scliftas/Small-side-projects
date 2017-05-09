#Keyword Encryption/Decryption Program
import time                                                                             #Imports the time module, allowing the script to be paused later on.
print("Welcome to this keyword encryption and decryption program!")                         
time.sleep(1)                                                                           #Pauses the script using the time module.
Message = input("Please type in the message you would like to encrypt or decrypt: ")    #Takes a user input for the message that they want to encrypt or decrypt.
Keyword = input("Please type in the keyword you want to use: ")                         #Takes a second user input for the keyword to use to encrypt or decrypt the Message.
while (len(Keyword)) < (len(Message)):                                                  #Creates a while loop so that if the keyword is not equal to the message, the follwing will be executed:
    Keyword = (Keyword + Keyword)                                                       #The keyword is stacked over and over until it's equal to the message and the while loop breaks.
Keyword  = Keyword[0:len(Message)]
UserInput = input("Type E to encrypt or D to decrypt: ")
if UserInput == ("E"):                                                                  #Checks if the user wants to encrypt a message.
    Message = Message.lower()
    Message = [ord(i)for i in Message]                                                  #Converts the user's message into the according ASCII table values.
    Message = [i - 96 for i in Message]                                                 #Subtracts 96 from every character in the message to get the position of the letters in the alphabet.
    Keyword = [ord(i)for i in Keyword]
    Keyword = [i - 96 for i in Keyword]
    Encryption = [x + y for x, y in zip(Message, Keyword)]                              #Combines every character in the message with the according character in the keyword.
    Encryption = [chr(i + 96)for i in Encryption]                                       #Converts the encrypted message into the according plaintext characters.
    Encryption = ''.join(Encryption)                 
    print("Your encrypted message is: ",Encryption)
    time.sleep(30)
elif UserInput == ("D"):                                                                #Checks if the user wants to decrypt if they didn't want to encrypt.
    Message = Message.lower()
    Message = [ord(i)for i in Message]
    Message = [i - 96 for i in Message]
    Keyword = [ord(i)for i in Keyword]
    Keyword = [i - 96 for i in Keyword]
    Decryption = [x - y for x, y in zip(Message, Keyword)]                                
    Decryption = [chr(i + 96)for i in Decryption]
    Decryption = ''.join(Decryption)
    print("Your decrypted message is: ",Decryption)
    time.sleep(30)
else:                                                                                   #Checks for any other input, which is counted as invalid and closes the program.
    print("Closing program...")
    time.sleep(10)
