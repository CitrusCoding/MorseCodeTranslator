#input the csv file into a dictionary 
def inputWords(csvFile): #Inputs words from csv into dictionary
    newDict = {}
    for words in csvFile:
        wordPairs = words.split(",")
        newDict[wordPairs[1].replace("\n", "")] = wordPairs[0]
    return (newDict)
    #morse : letters
#I took this directly from the helper function from the blackfoot dictionary project

#swap the key with the value
def swapPair(swapDict):
  newDict = dict([(value, key) for key, value in
                  swapDict.items()])
  return(newDict)
#took this from https://www.geeksforgeeks.org/python-program-to-swap-keys-and-values-in-dictionary/