def next_POI(listOfPOIs,currentIndex):
    print("list of poi length: ", len(listOfPOIs))
    print("current index + 1", (currentIndex+1))
    if (currentIndex+1) >= len(listOfPOIs):
        # print(listOfPOIs[0])
        newIndex = 0
        newPOI = listOfPOIs[newIndex]
        return newIndex, newPOI
    else:
        # print(listOfPOIs[currentIndex + 1])
        newIndex = currentIndex+1
        newPOI = listOfPOIs[newIndex]
        return newIndex, newPOI


# listOfPOIs = ["POI0","POI1"]
#
# next_POI(listOfPOIs, 0)
# next_POI(listOfPOIs, 2)