import string
from operator import itemgetter

#Constants
KEY = 0
VALUE = 1

def getFile():
    ''' 
        Reads in a file and handles the error if the file is not found.
    '''            
    filename = input("Enter filename: ")

    try:
        file_object = open(filename, "r")
        return file_object
    except:
        print("Filename {} not found!".format(filename))


def makeLists(file_object):
    ''' 
        Creation of lists from the object_file.
        First a list of paragraphs is created.
        Then a list of all the words in the data file.
    '''
    paragraphs = []
    cleandpara = []
    para = []
    newlist = []
    nlist = []

    for line in file_object:
        paragraphs = paragraphs + line.split()
        newlist = newlist + line.split()
        if line == "\n":
            para.append(paragraphs)
            paragraphs = []

    para.append(paragraphs)
    paragraphs = []

    for ob in para: #'Ob' resembles a whole paragraph, for lack of a better word.
        for word in ob:
            word = word.lower()
            word = word.strip()
            word = word.strip(string.punctuation)
            paragraphs.append(word)
        cleandpara.append(paragraphs)
        paragraphs = []

    for word in newlist:
        word = word.lower()
        word = word.strip()
        word = word.strip(string.punctuation)
        nlist.append(word)

    return nlist, cleandpara


def ParagraphIndex(wordlist, paralist):
    ''' 
        Creation of the paragraph index.
        Gets the lists from the makeLists() function
    '''
    tempword = ""
    sortedlist = []

    for word in wordlist:
        tempword = word
        for i in range(0,len(paralist)):
            if word in paralist[i]:
                tempword = tempword + " " + str(i+1) + ","
        if tempword not in sortedlist:
            sortedlist.append(tempword)
        tempword = ""

    return sortedlist


def printSortedList(sortedlist):
    ''' Printing of the paragraph index '''
    print("")
    print("The paragraph index: ")

    for ele in sorted(sortedlist):
        print(ele.strip(","))


def highest(wordlist):
    ''' 
        A function that creates the lists of top 10 and 20.
        Counts each word.
    '''
    toptenlist = []
    toptwentylist = []
    newlist = []
    countdict = {}

    for word in wordlist:
        try:
            countdict[word] += 1
        except KeyError:
            countdict[word] = 1

    for item in countdict.items():
        newlist.append(item)

    # Sorting the list by second element first in reverse, then by first element.
    newlist = sorted(newlist, key=lambda element: (-element[VALUE], element[KEY]))

    #Creation of top 10 list
    for i in range(0,10):
            toptenlist.append(newlist[i])

    #Creation of top 20 list
    for i in range(0,20):
        toptwentylist.append(newlist[i])

    return toptenlist, toptwentylist


def printHighestTen(topten):
    ''' Printing of the Top 10 most used words '''
    print("")
    print("The highest 10 counts: ")

    for ele in topten:
        print("{}: {}".format(ele[KEY],ele[VALUE]))


def printHighestTwenty(toptwenty):
    ''' Printing of the Top 20 most used words '''
    print("")
    print("The highest 20 counts: ")

    for ele in toptwenty:
        print("{}: {}".format(ele[KEY],ele[VALUE]))


def main():
    #Main function here
    file_object = getFile()

    if file_object:
        wordlist, paralist = makeLists(file_object)

        sortedlist = ParagraphIndex(wordlist, paralist)

        topten, toptwenty = highest(wordlist)

        printSortedList(sortedlist)

        printHighestTen(topten)

        printHighestTwenty(toptwenty)


main()