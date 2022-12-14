#CURRENT STATUS: translation works both ways, no other features implemented. User interface is incomplete.
#Update: if you type too long of a message in morse->english it breaks the program for some reason ? only sometimes apperently
#update 2:nevermind its not doing it anymore? probably something specific, check it later I guess

#A third attempt at my (morse) code translator program that I technically started working on in Grade 11 lol :)))
#combines elements from my Grade 11 "Whale Talk" js program and my CMPT 120 "Blackfoot Dictionary" final proj.
#anyway welcome to the show folks

#the plan:
#basic translate functions (eng->morse and morse->eng)
#a test function
#a learn function
# ^ basically the same as dictionary proj
#there needs to be an explination of the format:
#- . = dot, - = dash, / = space between words
#note: do we want this program to have any visual elements? THis would have been a lot easier in html but it is possible with pygame I think - maybe make 2 versions with and without, just cause I can

#BEGINNING OF PROGRAM 

#Imports
import dictFuncs

#Variables
keepGoing = True #flag variable
#testScore = 0  #for future test function
switchBack = False #track when keys and values are switched
currentDict = dictFuncs.inputWords(
    open("MorseCode.csv"))  #turns csv into dictionary w/helper function
#if you want to add more codes aside from morse then make a folder for them and change it to open("folder/code.csv")

#User Interface
#welcome message
print("Hello\nwelcome to the morse code translator!")
print(
    ".... . .-.. .-.. ---\n.-- . .-.. -.-. --- -- . / - --- / - .... . / -- --- .-. ... . / -.-. --- -.. . / - .-. .- -. ... .-.. .- - --- .-."
)
#describe what it does a little probably, tell users what

#take inputs
#return output
#offer different possible options ? I would like a test function, an audio/flashing image function would actually be cool too, consider (may require pygame :P - at least I have a reference from the prev proj.)

#run the program until the user decides to close it by typing "exit"
while (keepGoing):
    print("")
    print("\nI want to: ")
    taskChoice = input("options: translate/learn/exit\n") #lists options

    #Translate
    if (taskChoice.lower() == "translate"):
        whichTrans = input("\ndo you want to translate English to morse code, or morse code to English?\n")
        invalidTransInput = True #sets it to true by default so the loop runs

        #loop until input is valid
        while (invalidTransInput):
          
          #translate English to morse code
          if (whichTrans.lower() == "to morse" or whichTrans.lower() == "morse" or whichTrans.lower() == "english to morse code"):
            
            #switch letters to keys and morse to values
            if (switchBack == False): 
              currentDict = dictFuncs.swapPair(currentDict)
              switchBack = True; #note that it needs to be switched back to morse:

            #take user input
            transPhrase = input("Input the word/phrase you want translated:\n")
            
            #seperates words into letters
            transList = list(transPhrase)
            invalidTransInput = False


          #translate morse code to English
          elif (whichTrans.lower() == "to english" or whichTrans.lower() == "english" or whichTrans.lower() == "morse code to english"):

            #if the directory was switched to letters:morse switch it back to morse:letters
            if (switchBack):
              currentDict = dictFuncs.swapPair(currentDict)
              switchBack = False; 

            #take user input
            transPhrase = input("Input the word/phrase you want translated:\n")
            
            #seperates letters into their own strings
            transList = transPhrase.split(" ")
            
            invalidTransInput = False
            #dict is in the correct order by default


          #invalid input
          else:
            print("Invalid Input: please write 'to english' or 'to morse'")
            
            #ask for input again
            whichTrans = input("do you want to translate English to morse code, or morse code to English?\n")
            invalidTransInput = True


        #print translation 
        for letter in transList:
            #check to see if character is valid
            if (letter.upper() in currentDict.keys()):
                print(currentDict[letter.upper()], end=" ")
            else:
                print("?", end=" ")

    #Learn
    if (taskChoice.lower() == "learn"):
      for x in currentDict:
        if(x == "/"):
          print(x + " indicates the blank space between words")
        else:
          print(currentDict[x] + " is " + x)

    #learn function (type in a letter, be shown the morse equivalent and vice versa)

    #test function (show a letter, have users type the corresponding symbol and vice versa)

    #learn and test should be very similar I think

    if (taskChoice.lower() == 'exit'):
      keepGoing = False

#END OF PROGRAM
