from textblob import TextBlob

def correct_spelling(text):
    blob = TextBlob(text)
    return str(blob.correct())

# Example usage
text = "I havv a speling errror"
print("Original:", text)
print("Corrected:", correct_spelling(text))
