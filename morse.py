morseDict = {"A":".- ", "B":"-... ", "C":"-.-. ", "D":"-.. ", "E":". ", "F":"..-. ", "G":"--. ", "H":".... ", "I":".. ", "J":".--- ", "K":"-.-. ", "L":".-.. ", "M":"-- ", "N":"-. ", "O":"--- ", "P":".--. ", "Q":"--.- ", "R":".-. ", "S":"... ", "T":"- ", "U":"..- ", "V":"...-", "W":".-- ", "X":"-..- ", "Y":"-.-- ", "Z":"--.. ", " ":"/ "}

Msg = input(str("Message to translate: "))
Msg = Msg.upper()

for i in Msg:
    print(morseDict[i], end="")