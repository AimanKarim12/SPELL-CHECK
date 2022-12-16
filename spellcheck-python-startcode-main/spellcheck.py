# Spell Check Starter
# This start code creates two lists
# 1: dictionary: a list containing all of the words from "dictionary.txt"
# 2: aliceWords: a list containing all of the words from "AliceInWonderland.txt"

import re  # Needed for splitting text with a regular expression
import time

def main():
    # Load data files into lists
    dictionary = loadWordsFromFile("data-files/dictionary.txt")
    aliceWords = loadWordsFromFile("data-files/AliceInWonderLand.txt")

    # MAIN PROGRAM LOOP
    loop = True
    while loop: 
        selection = getMenuSelection()

        if selection == "1":
            checkWordLinear(dictionary)
        elif selection =="2":
            checkWordBinary(dictionary)
        elif selection =="3":
            checkWordLinearAIW(aliceWords)
        elif selection =="4":
            checkWordBinaryAIW(aliceWords)
            

# end main()

def getMenuSelection():
    #PRINT MAIN MENU
    print("MAIN MENU")
    print("1. Spell Check a Word (Linear Search)")
    print("2. Spell Check a Word (Binary Search)")
    print("3. Spell Check Alice In Wonderland (Linear Search)")
    print("4. Spell Check Alice In Wonderland (Binary Search)")

    #USER INPUT 
    return input("Enter Selection (1-4): ")

#LINEAR 
def checkWordLinear(dictionary):
    print("LINEAR SEARCH A WORD")
    userinput = input("Enter A Word: ")
    
    print("Linear Search is Starting..")
    start = time.time()
    result = linearSearch(dictionary, userinput.lower())
    end = time.time()
    if(result == -1):
        print(userinput, "Is Not Found")
    else:
        print(userinput, "Is Found At: ", result)
    print("it took" , end - start, "Seconds")

#BINARY
def checkWordBinary(dictionary):
    print("BINARY SEARCH A WORD")
    userinput = input("Enter A Word: ")
    print("BINARY Search is Starting..")
    start = time.time()
    result = binarySearch(dictionary, userinput.lower())
    end = time.time()

    if result != -1:
        print(userinput, "Is Found At", str(result))

    else:
        print(userinput, "Is Not Found")
        
    print("it took" , end - start, "Seconds")

#LINEAR AIW
def checkWordLinearAIW(dictionary, aliceWords):
    count = 0
    print("Linear Search is Starting..")
    for word in aliceWords:
        start = time.time()
        result = linearSearch(dictionary, word)
        end = time.time()
        if(result == -1):
            print(word, "Is Not Found")
    else:
        count += 1
        print(f"total words from Alice Words Not In Dictionary: {count}")
        print("it took" , end - start, "Seconds")


#BINARY AIW
def checkWordBinaryAIW(aliceWords):
    print("BINARY SEARCH A WORD")
    userinput = input("Enter A Word: ")
    print("BINARY Search is Starting..")
    start = time.time()
    result = binarySearch(aliceWords, userinput.lower())
    end = time.time()

    if result != -1:
        print(userinput, "Is Found At", str(result))

    else:
        print(userinput, "Is Not Found")
        
    print("it took" , end - start, "Seconds")


def loadWordsFromFile(fileName):
    # Read file as a string
    fileref = open(fileName, "r")
    textData = fileref.read()
    fileref.close()

    # Split text by one or more whitespace characters
    return re.split('\s+', textData)
# end loadWordsFromFile()

def linearSearch(aList, item):
    for i in range(len(aList)):
        if (aList[i] == item):
            return i
    return -1

def binarySearch(array, item):
        
    top = len(array) - 1
    mid = 0
    bottom = 0
        
    while bottom <= top:
        mid = (top + bottom) // 2
        if array[mid] < item:
            bottom = mid + 1
        elif array[mid] > item:
            top = mid - 1
        else:
            return mid
        return -1


# Call main() to begin program
main()
