### Cheeky python answer ###

# myList = [1,2,3,4]

# def reverseOrder(listToReverse):
#     myList = list(listToReverse)
#     myList.reverse()
#     print(myList)
#     return myList


# reverseOrder(myList)


myString = "abcdefg"

def myReverse(stringToReverse):
    newString = ""
    for x in range(len(myString)):
        newString = myString[x] + newString
    print(myString)
    print(newString)

myReverse(myString)

