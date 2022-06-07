# Input : list of POIs, list of place IDs, list of Coordinates, list of ratings, list of types
# The goal of this function is to shuffle those list while preserving their link
# The shuffle should be affected by the google rating of each POI
# This function is only used in the implementation with happy mapping of the chat bot
import random

listOfPOIs = ["popular POI", "mediumly popular POI", "unpopular POI"]
listOfPlaceIDs = ["ID1", "ID2", "ID3"]
listOfCoordinates = [[1,1], [2,2], [3,3]]
listOfRatings = [5, 3, 1]
listOfUserRatingsNumber = [1, 2, 3]
listOfTypes = ["type1", "type2", "type3"]

def shuffle_POI(listOfPOIs, listOfPlaceIDs, listOfCoordinates, listOfRatings, listOfUserRatingsNumber, listOfTypes):
    finalListOfPOIs = []
    finalListOfPlaceIDs = []
    finalListOfCoordinates = []
    finalListOfRatings = []
    finalListOfUserRatingsNumber = []
    finalListOfTypes = []

    while listOfPOIs:
        # choose one of the elements at random (with google ratings as weights), create a 1 element list, take its first element
        chosen_element = random.choices(listOfPOIs, weights=listOfRatings, k=1)[0]
        chosen_element_index = listOfPOIs.index(chosen_element)
        print("chosen element: ", chosen_element)
        print("index of the chosen element: ", chosen_element_index)
        # print(listOfPOIs[0])
        # remove first element of list
        finalListOfPOIs.append(listOfPOIs[chosen_element_index])
        finalListOfPlaceIDs.append(listOfPlaceIDs[chosen_element_index])
        finalListOfCoordinates.append(listOfCoordinates[chosen_element_index])
        finalListOfRatings.append(listOfRatings[chosen_element_index])
        finalListOfUserRatingsNumber.append(listOfUserRatingsNumber[chosen_element_index])
        finalListOfTypes.append(listOfTypes[chosen_element_index])

        listOfPOIs.pop(chosen_element_index)
        listOfPlaceIDs.pop(chosen_element_index)
        listOfCoordinates.pop(chosen_element_index)
        listOfRatings.pop(chosen_element_index)
        listOfUserRatingsNumber.pop(chosen_element_index)
        listOfTypes.pop(chosen_element_index)



    return finalListOfPOIs, finalListOfPlaceIDs, finalListOfCoordinates, finalListOfRatings, finalListOfUserRatingsNumber, finalListOfTypes

    # print('removed everything')


listOfPOIs, listOfPlaceIDs, listOfCoordinates, listOfRatings, listOfUserRatingsNumber, listOfTypes = shuffle_POI(listOfPOIs, listOfPlaceIDs, listOfCoordinates, listOfRatings, listOfUserRatingsNumber, listOfTypes)

print("listOfPOIs : ", listOfPOIs)
print("listOfPlaceIDs: ", listOfPlaceIDs)
print("listOfCoordinates: ", listOfCoordinates)
print( "listOfRatings:", listOfRatings)
print("listOfUserRatingsNumber: ", listOfUserRatingsNumber)
print("listOfTypes : ", listOfTypes)