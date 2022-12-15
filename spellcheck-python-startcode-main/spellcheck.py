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

        
# end main()

def getMenuSelection():
    #PRINT MAIN MENU
    print("MAIN MENU")
    print("1. Spell Check a Word (Linear Search)")
    print("2. Spell Check a Word (Binary Search)")
    print("3. Spell Check Alice In Wonderland (Linear Search)")
    print("4. Spell Check Alice In Wonderland (Binary Search)")
    print("5. Exit")

    #USER INPUT 
    return input("Enter Selection (1-5): ")

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



# PART A   
# LOOP
loop = True
while loop: 

#USER INPUT 
    select = input("Enter Selection (1-5): ")
    
    #LINEAR SEARCH
    if select == "1":
        print("LINEAR SEARCH")
        start = time.time()
        userinput = input("Enter A Word: ")
        def linearSearch(dictionary, userinput):
            for i in range(len(dictionary)):
                if (dictionary[i] == userinput):
                    return i
            return -1

        dictionary = loadWordsFromFile("data-files/dictionary.txt")
        result = linearSearch(dictionary, userinput)
        if(result == -1):
            print("Linear Search is Starting..")
            print(userinput, "Is Not Found")
            end = time.time()
            print("it took" , end - start, "Seconds")
        else:
            print("Linear Search is Starting..")
            print(userinput, "Is Found At: ", result)
            end = time.time()
            print("it took" , end - start, "Seconds")
    
    #BINARY SEARCH
    elif select == "2":
        print("BINARY SEARCH")
        start = time.time()
        userinput = input("Enter A Word: ")
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
            
        dictionary = loadWordsFromFile("data-files/dictionary.txt")
        item = userinput

        result = binarySearch(dictionary, item)

        if result != -1:
            print("BINARY Search is Starting..")
            print(userinput, "Is Found At", str(result))
            end = time.time()
            print("it took" , end - start, "Seconds")
        else:
            print("BINARY Search is Starting..")
            print(userinput, "Is Not Found")
            end = time.time()
            print("it took" , end - start, "Seconds")

    #PART B
    #LINEAR SEARCH  AIW
    elif select == "3":
        print("LINEAR SEARCH (ALICE IN WONDERLAND)")
        start = time.time()
        userinput = input("Enter A Word: ")
        def linearSearch(aliceWords, userinput):
            for i in range(len(aliceWords)):
                if (aliceWords[i] == userinput):
                    return i
            return -1

        aliceWords = loadWordsFromFile("data-files/AliceInWonderLand.txt")
        result = linearSearch(aliceWords, userinput)
        number_of_elements = len(aliceWords)
        if(result == -1):
            print("Linear Search is Starting..")
            print(userinput, "Is Not Found")
            end = time.time()
            print("it took" , end - start, "Seconds")
        else:
            print("Linear Search is Starting..")
            print("Number of the word:", userinput, "in the list: ", number_of_elements)
            end = time.time()
            print("it took" , end - start, "Seconds")
    
    #BINARY SEARCH AIW
    elif select == "4":
        print("BINARY SEARCH (ALICE IN WONDERLAND)")
        start = time.time()
        userinput = input("Enter A Word: ")
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
            
        aliceWords = loadWordsFromFile("data-files/AliceInWonderLand.txt")
        item = userinput

        result = binarySearch(aliceWords, item)
        number_of_elements = len(userinput)

        if result != -1:
            print("BINARY Search is Starting..")
            print("Number of the word:", userinput, "in the list: ", number_of_elements)
            end = time.time()
            print("it took" , end - start, "Seconds")
        else:
            print("BINARY Search is Starting..")
            print(userinput, "Is Not Found")
            end = time.time()
            print("it took" , end - start, "Seconds")
    
    
    #EXIT
    elif select == "5":
        print ("EXIT")
 
        loop = False
