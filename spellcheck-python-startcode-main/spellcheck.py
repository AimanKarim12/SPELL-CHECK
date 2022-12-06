# Spell Check Starter
# This start code creates two lists
# 1: dictionary: a list containing all of the words from "dictionary.txt"
# 2: aliceWords: a list containing all of the words from "AliceInWonderland.txt"

import re  # Needed for splitting text with a regular expression


def main():
    # Load data files into lists
    dictionary = loadWordsFromFile("data-files/dictionary.txt")

    #aliceWords = loadWordsFromFile("data-files/AliceInWonderLand.txt")

    # Print first 50 values of each list to verify contents
    print(dictionary[0:50])
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

# PART A   
# LOOP
loop = True
while loop: 
#USER INPUT 
    userinput = input("Enter A Word: ")
    select = input("Select 1 for Linear Search, Select 2 For Binary Search: ")
    
    #LINEAR SEARCH
    if select == "1":
        def linearSearch(dictionary, userinput):
            for i in range(len(dictionary)):
                if (dictionary[i] == userinput):
                    return i
            return -1

        dictionary = loadWordsFromFile("data-files/dictionary.txt")
        result = linearSearch(dictionary, userinput)
        if(result == -1):
            print(userinput, "Is Not Found")
        else:
            print(userinput, "Is Found At: ", result)
    
    #BINARY SEARCH
    elif select == "2":
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
                return - 1
            
        dictionary = loadWordsFromFile("data-files/dictionary.txt")
        item = userinput

        result = binarySearch(dictionary, item)

        if result != -1:
            print(userinput, "Is Found At", str(result)) 
        else:   
            print(userinput, "Is Not Found")
 
        loop = False