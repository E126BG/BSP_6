import difflib as dl

close_match = dl.get_close_matches("Hello", ["them", "those", "this"], cutoff=0.5, n=1)


def correct_sentence_difflib(sentence, list_of_words):
    sentence = sentence.split()
    # print(sentence)
    corrected_sentence = []
    for word in sentence:
        # print("word: ", word)
        corrected_word = dl.get_close_matches(word, list_of_words, cutoff=0.5, n=1)
        # print("corrected words: ", corrected_word)
        if corrected_word:
            # corrected_sentence += corrected_word
            corrected_sentence.append(corrected_word[0])
        else:
            # corrected_sentence += word #culprit
            corrected_sentence.append(word)
    corrected_sentence_string = ""
    for word in corrected_sentence:
        corrected_sentence_string += word + " "


    # print(corrected_sentence_string)
    return corrected_sentence_string

# sentence = correct_sentence_difflib("Hello I am Eliott and I live in paiis", ["paris", "london", "esch-sur-alzette"])
# print(sentence)