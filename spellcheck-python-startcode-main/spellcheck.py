# Spell Check Starter
# This start code creates two lists
# 1: dictionary: a list containing all of the words from "dictionary.txt"
# 2: aliceWords: a list containing all of the words from "AliceInWonderland.txt"

import re  # Needed for splitting text with a regular expression


def main():
    # Load data files into lists
    dictionary = loadWordsFromFile("data-files/dictionary.txt")

    aliceWords = loadWordsFromFile("data-files/AliceInWonderLand.txt")

    # Print first 50 values of each list to verify contents
    #print(dictionary[0:50])
    #print(aliceWords[0:50])

# end main()


def loadWordsFromFile(fileName):
    # Read file as a string
    fileref = open(fileName, "r")
    textData = fileref.read()
    fileref.close()

    # Split text by one or more whitespace characters
    return re.split('\s+', textData)
# end loadWordsFromFile()


# Call main() to begin program
main()

#TIME
import time

# PART A   
# LOOP
loop = True
while loop: 

    #PRINT MAIN MENU
    print("MAIN MENU")
    print("1. Spell Check a Word (Linear Search)")
    print("2. Spell Check a Word (Binary Search)")
    print("3. Spell Check Alice In Wonderland (Linear Search)")
    print("4. Spell Check Alice In Wonderland (Binary Search)")
    print("5. Exit")

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
    
    
    #EXIT
    elif select == "5":
        print ("EXIT")
 
        loop = False

