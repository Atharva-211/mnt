import math

d = list()
d.append('An apple a day keeps the doctor away'.lower().split(' '))
d.append('Never compare an apple to an orange'.lower().split(' '))
d.append('I prefer scikit-learn to orange'.lower().split(' '))
compDoc = "I'd like an apple and a doctor".split(' ')

terms = set()
tf = []  # Will store the term frequency dictionaries for each document

# First, collect all unique terms
for doc in d:
    for item in doc:
        terms.add(item)

# Then compute term frequencies for each document
for doc in d:
    temp = {}  # Create a new dictionary for each document
    for item in doc:
        temp[item] = doc.count(item)/len(doc)
    tf.append(temp)  # Add this document's term frequencies to the list

# Compute IDF values
idf = {}
for term in terms:
    doc_count = 0
    for doc in d:
        if term in doc:
            doc_count += 1
    idf[term] = 1 + math.log(len(d)/doc_count)

# Calculate TF-IDF scores for comparison
tfidf = [0, 0, 0]
for term in compDoc:
    for i in range(len(d)):
        if term in tf[i]:  # Check if the term exists in document i's term frequency dict
            tfidf[i] += tf[i][term] * idf[term]

print(f"TF-IDF scores: {tfidf}")
print(f"Document with highest similarity: {tfidf.index(max(tfidf))+1}")
