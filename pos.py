import nltk
from nltk import word_tokenize, pos_tag

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

def pos_tagging(sentence):
    tokens = word_tokenize(sentence)
    tagged = pos_tag(tokens)
    return tagged

# Example usage
sentence = "The quick brown fox jumps over the lazy dog"
print("POS Tags:", pos_tagging(sentence))