import spacy

nlp = spacy.load('en_core_web_sm')

# Example 1

doc = nlp(u'How are you doing today?')

for token in doc:
    print(token.text, token.vector[:5])

# Example 2

hello_doc = nlp(u'hello')
hi_doc = nlp(u'hi')
hella_doc = nlp(u'hella')

print(hello_doc.similarity(hi_doc))
print(hello_doc.similarity(hella_doc))

# Example 3

Got_str1 = nlp(u'when will next season of Game of Thrones be releasing')
Got_str2 = nlp(u'Game of Thrones next season release date?')

print(Got_str1.similarity(Got_str2))

example_doc = nlp(u'car truck google')
for t1 in example_doc:
    for t2 in example_doc:
        similarity_perc = int(t1.similarity(t2)*100)
        print("Word {} is {}% similar to word {}".format(t1.text, similarity_perc, t2.text))
