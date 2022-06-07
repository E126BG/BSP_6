def checkSynonyms(city):
    city = city.lower()
    # add synonyms by couple, first the unrecognized name, then the recognized one
    synonyms = [["esch", "esch sur alzette"], ["luxembourg", "luxembourg city"]]
    #compare input to every unofficial city appellation stored
    for i in range(len(synonyms)):
        if city == synonyms[i][0]:
            return synonyms[i][1]
    return city


print(checkSynonyms("Esch"))