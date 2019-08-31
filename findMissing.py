# findMissing(
# [4,12,9,5,6],
# [4,9,12,6]
# ) => 5

array1 = [4,12,9,5,6,44]
array2 = [4,9,12,6,44]
 
def find_missing(array1, array2):
    found = []
    missing = []
    
    for x in range(len(array1)):
        lookingFor = array1[x]
        for y in range(len(array2)):
            testInput = array2[y]
            if lookingFor == testInput:
                found.append(lookingFor)                
                print("found " + str(lookingFor))
                break
            elif lookingFor != testInput and y == len(array2) - 1:
                print("did not find " + str(lookingFor))
                missing.append(lookingFor)


find_missing(array1, array2)