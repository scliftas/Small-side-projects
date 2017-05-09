#Binary Search program
userinput = input("Please think of a number between 1 and 100.")
print("I shall now try to guess the number that you are thinking of.")
maximumnumber = int(100)
minimumnumber = int(1)
tries = int(0)
middlepoint = int(round(maximumnumber + minimumnumber) / 2)
print(middlepoint)
while userinput != middlepoint:
    useranswer = input("Is my guess too high or too low?")
    if useranswer == ("too low"):
        minimumnumber = middlepoint
        middlepoint = int(round(maximumnumber + minimumnumber) / 2)
        print(middlepoint)
        tries = tries + 1
    elif useranswer == ("too high"):
        maximumnumber = middlepoint
        middlepoint = int(round((maximumnumber + minimumnumber) / 2))
        print(middlepoint)
        tries = tries + 1
    else:
        print("I have successfully guessed your number, it took me",tries,"tries.")
        break
print("Thank you for playing this game.")
