# This actions finds the coordinates of a place simply by inputing its name (ex : "Paris")

# importing geopy library
import json

from geopy.geocoders import Nominatim
import requests
import googlemaps

def find_coordinates(place):
    str(place)
    # calling the Nominatim tool
    loc = Nominatim(user_agent="GetLoc")

    # entering the location name
    getLoc = loc.geocode(place)

    # printing address
    print(getLoc.address)

    # printing latitude and longitude


    return getLoc.latitude, getLoc.longitude


def create_querry(place, POI):

    latitude, longitude = find_coordinates(place)

    url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=" + str(latitude) + ',' + str(longitude) + '&radius=1500&type=' + str(POI) + '&key=AIzaSyAslp2WJu3GNbrL1pOgEOMmFmSMSZ7hOuM'
    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    return response

# def find_museums(place):
#     payload = {}
#     headers = {}
#
#     # writes the query result as a file
#     response = create_querry(place, "museum")
#     with open('json_data.json', 'w') as outfile:
#         json.dump(response.text, outfile)
#
#     #declaration of the list
#     listOfMuseums = []
#
#     with open('json_data.json') as json_file:
#         # converts file to string
#         data = json.load(json_file)
#         # converts string to dictionary
#         y = json.loads(data)
#         # parse the dictionary
#         for key in y["results"]:
#             listOfMuseums.append(key["name"])
#         if(listOfMuseums):
#             print(listOfMuseums[0])
#             return listOfMuseums
#         else:
#             return ["Did not find any"]

def find_POI(place, POI):
    payload = {}
    headers = {}

    # writes the query result as a file
    response = create_querry(place, POI)
    print(response.text)
    with open('json_data.json', 'w') as outfile:
        json.dump(response.text, outfile)

    #declaration of the lists
    # POI names
    listOfPOIs = []
    # POI PlaceIDs (used to obtain extra info on google maps)
    listOfPlaceIDs = []
    # POI coordinates [lat, lgn]
    listOfCoordinates = []
    #POI google ratings
    listOfRatings = []
    #POI number of users that rated it
    listOfUserRatingsNumber = []
    #POI types
    listOfTypes = []


    with open('json_data.json') as json_file:
        # converts file to string
        data = json.load(json_file)
        # converts string to dictionary
        y = json.loads(data)
        # parse the dictionary
        for key in y["results"]:
            listOfPOIs.append(key["name"])
            listOfPlaceIDs.append(key["place_id"])
            listOfCoordinates.append([key["geometry"]["location"]["lat"],key["geometry"]["location"]["lng"]])
            listOfTypes.append(key["types"])
            # In case the POI was never rated, rating and user_ratings_total will not be in the json
            # We have to take that into account
            try:
                key["rating"]
            except KeyError:
                listOfRatings.append("0")
                listOfUserRatingsNumber.append("0")
            else:
                listOfRatings.append(key["rating"])
                listOfUserRatingsNumber.append(key["user_ratings_total"])

        if(listOfPOIs):
            print(listOfPOIs[0])
            print(listOfPlaceIDs[0])
            print(listOfCoordinates[0])
            print(listOfRatings[0])
            print(listOfUserRatingsNumber[0])
            nbOfPOIs = len(listOfPOIs)
            print("number of POIs",nbOfPOIs)
            return (nbOfPOIs, listOfPOIs, listOfPlaceIDs, listOfCoordinates, listOfRatings, listOfUserRatingsNumber, listOfTypes)
        else:
            return ["Did not find any"]







# latitude, longitude = find_coordinates("london")
#
# print("Latitude = ", latitude, "\n")
# print("Longitude = ", longitude)

find_POI("esch-sur-alzette", "museum")

# Create googleAPI query




# find_museums("Zurich")

# # Opening JSON file
# f = open('json_data.json')
#
# # returns JSON object as
# # a dictionary
# data = json.load(f)
#
# # Iterating through the json
# # list

#
# # Closing file
# f.close()