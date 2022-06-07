def tell_about_types(listOfTypes):
    sentence = f"It has been qualified as a {listOfTypes[0]}"

    if len(listOfTypes) >= 2 :
        for i in listOfTypes[1:-1]:
            sentence += f", a {i}"
        sentence += f" and a {listOfTypes[-1]}"

    return sentence



# tell_about_types(["one", "two", "three", "four", "five"])
# tell_about_types(["one"])
# tell_about_types(["one", "two"])