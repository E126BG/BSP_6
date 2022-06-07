from textblob import TextBlob

def correct_sentence_textblob(sentence):
    blob = TextBlob(sentence)
    blob = blob.correct()
    print(blob)

# correct_sentence_textblob("I live in landon")
# correct_sentence_textblob("esch-sur-alzette")
# correct_sentence_textblob("I'd like to live in pris")
# correct_sentence_textblob("lxembourg city")