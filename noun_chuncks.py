import spacy

nlp = spacy.load('en_core_web_sm')

# Example 1
doc = nlp(u'Bostom Dynamics is gearing up to produce thousands of robots dogs')

for chunk in doc.noun_chunks:
    print(chunk.text,chunk.root.text,chunk.root.dep_,chunk.root.head.text)

# Example 2
doc2 = nlp(u'Deep Learning cracks the code of messenger RNAs and protein-coding potential')

for chunk in doc2.noun_chunks:
    print(chunk.text, chunk.root.text, chunk.root.dep_, chunk.root.head.text)

