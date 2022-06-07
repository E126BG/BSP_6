
def google_maps_search_coordinates(long, lat):
    # A less precise version if we do not have the placeID of the POI
    search_url = f"https://www.google.com/maps/search/?api=1&query={long}%2C{lat}"
    return search_url

# google_maps_search_coordinates(49.49931040000001, 5.9771982)

def google_maps_search_placeID(long, lat, placeID):
    search_url = f"https://www.google.com/maps/search/?api=1&query={long}%2C{lat}&query_place_id={placeID}"
    # print(search_url)
    return search_url


# google_maps_search_placeID(49.49931040000001,5.9771982, "ChIJn2-lyBo1lUcRnZ4RyRzvflM")