from textblob import TextBlob

# misspelled words
blob = TextBlob("I have a guud ideea")

# perform spelling correction
corrected_blob = blob.correct()

# print the corrected text
print("Original Text:", blob)
print("Corrected Text:", corrected_blob)