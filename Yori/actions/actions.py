# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
# This will be used to store some contextual informations in slots, in order to use them throughout the interaction
from rasa_sdk.events import SlotSet

import datetime as dt
from . import find_coordinates
from . import check_synonyms
from . import correct_sentence_difflib
from . import next_POI
from . import google_maps_search_coordinates
from . import tell_more_POI

# needed in order to recognize the city (in case it's misspelled)
cities_list = ["luxembourg city", "esch", "luxembourg", "esch-sur-alzette", "esch sur alzette", "dudelange",
               "differdange", "schifflange", "bettembourg", "petange", "ettelbruck", "diekirch", "strassen",
               "bertrange", "belvaux", "mamer", "soleuvre", "echternach", "wiltz", "bascharage", "rodange", "oberkorn",
               "rumelange", "kayl", "howald", "grevenmacher", "bereldange", "mersch", "mondercange", "niederkorn",
               "remich", "bridel", "tetange", "mondorf-les-bains", "mondorf les bains", "sandweiler", "bissen", "sanem",
               "lamadelaine", "junglinster", "wasserbillig", "steinfort", "helmsange", "hesperange", "leudelange",
               "steinsel", "itzig", "clemency", "colmar-berg", "lintgen", "kehlen", "heisforf", "senningerberg",
               "eischen", "vianden", "niederanwen", "bergem", "hautcharage", "mertzig", "gonderange", "beaufort",
               "troisvierges", "larochette", "schieren", "alzingen", "capellen", "frisange", "fentange", "dalheim",
               "crauthem", "consdorf", "warken", "moutfort", "mertert", "redange", "niederfeulen", "contern",
               "bettendorf", "koerich", "clervaux", "hobscheid", "schrassig", "mullendorf", "paris", "amsterdam",
               "london", "berlin"]
listOfPOIs = []
listOfPlaceIDs = []
listOfCoordinates = []
listOfRatings = []
listOfUserRatingsNumber = []
listOfTypes = []
currentIndex = 0


class ActionExhibitionSearch(Action):
    def name(self) -> Text:
        return "action_exhibition_search"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        facility = tracker.get_slot("POI")
        address = "300 Hyde St, San Francisco"
        dispatcher.utter_message(text="Here is the address of the {}:{}".format(facility, address))

        return [SlotSet("address", address)]


class ActionExhibitionLocation(Action):
    def name(self) -> Text:
        return "action_exhibition_location"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Exhibition is at this location!")

        return []


class ActionGiveTime(Action):
    def name(self) -> Text:
        return "action_give_time"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text=f"The current time is {dt.datetime.now().strftime('%H:%M:%S')}")

        return []


class ActionTellMuseumLocation(Action):
    def name(self) -> Text:
        return "action_tell_museum_location"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        global listOfPOIs

        current_location = next(tracker.get_latest_entity_values("location"), None)
        listOfPOIs = find_coordinates.find_museums(current_location)
        # msg = f"I understood you're looking for a museum in {current_location}"
        msg = f"Here is the top museum of {current_location}: {listOfPOIs[0]}"
        dispatcher.utter_message(text=msg)

        return []


# need to create an action "correct message of user" that does not need to detect any entity.
# then somehow extract the entities from this message and not the user's input.

class ActionCorrectUserInput(Action):
    def name(self) -> Text:
        return "action_correct_user_input"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        #
        # current_location = tracker.get_slot("place")
        # current_location = check_synonyms.checkSynonyms(current_location)
        # current_location = correct_sentence_difflib.correct_sentence_difflib(current_location, cities_list)
        # current_POI = tracker.get_slot("PointOfInterest")
        # listOfPOI = find_coordinates.find_POI(current_location, current_POI)
        corrected_message = correct_sentence_difflib.correct_sentence_difflib(tracker.latest_message.text, cities_list)
        dispatcher.utter_message("Here is the corrected message: ")
        dispatcher.utter_message(text=corrected_message)

        return []


class ActionTellPOILocation(Action):
    def name(self) -> Text:
        return "action_tell_POI_location"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        global listOfPOIs
        global listOfCoordinates
        global listOfPlaceIDs
        global listOfRatings
        global listOfUserRatingsNumber
        global listOfTypes

        current_location = tracker.get_slot("place")
        current_location = check_synonyms.checkSynonyms(current_location)
        current_location = correct_sentence_difflib.correct_sentence_difflib(current_location, cities_list)
        current_POI = tracker.get_slot("PointOfInterest")
        (nbOfPOIs, listOfPOIs, listOfPlaceIDs, listOfCoordinates, listOfRatings, listOfUserRatingsNumber,
         listOfTypes) = find_coordinates.find_POI(current_location, current_POI)
        msg = f"There are {nbOfPOIs} places that correspond to your querry"

        msg1 = f"Here is the top rated {current_POI} of {current_location}: {listOfPOIs[0]}"

        msg2 = f"Type next to see the next POI, show maps to show its location or more info to see the tags of the POI"
        dispatcher.utter_message(text=msg)
        dispatcher.utter_message(text=msg1)
        dispatcher.utter_message(text=msg2)

        return []


class ActionNextPOI(Action):
    def name(self) -> Text:
        return "action_next_POI"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        global currentIndex
        global listOfPOIs
        currentIndex, current_POI = next_POI.next_POI(listOfPOIs, currentIndex)

        msg = f"Next POI: {current_POI}, index : {currentIndex}"
        msg1 = f"Type next to see the next POI, show maps to show its location or more info to see the tags of the POI"
        dispatcher.utter_message(msg)
        dispatcher.utter_message(msg1)

        return [SlotSet("PointOfInterest", current_POI)]


class ActionShowLocation(Action):
    def name(self) -> Text:
        return "action_show_location"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        search_url = google_maps_search_coordinates.google_maps_search_placeID(listOfCoordinates[currentIndex][0],
                                                                               listOfCoordinates[currentIndex][1],
                                                                               listOfPlaceIDs[currentIndex])
        msg = f"Here are the coordinates of {listOfPOIs[currentIndex]}: {search_url}"
        dispatcher.utter_message(msg)

        return []

class ActionTellMore(Action):
    def name(self) -> Text:
        return "action_tell_more"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        search_url = google_maps_search_coordinates.google_maps_search_placeID(listOfCoordinates[currentIndex][0],
                                                                               listOfCoordinates[currentIndex][1],
                                                                               listOfPlaceIDs[currentIndex])
        msg = f"{listOfPOIs[currentIndex]} is a Point Of Interest that was awarded a rating of {listOfRatings[currentIndex]} by {listOfUserRatingsNumber[currentIndex]} different visitors."
        dispatcher.utter_message(msg)

        msg = str(listOfTypes[currentIndex])
        dispatcher.utter_message(msg)


        msg = tell_more_POI.tell_about_types(listOfTypes[currentIndex])
        dispatcher.utter_message(msg)




        return []