import spacy
nlp = spacy.load('en_core_web_sm', disable=['ner', 'tagger', 'parser', 'lemmatizer'])
lemmatizer = nlp.get_pipe('lemmatizer')
t = nlp('chuckles')[0]
t.pos_ = 'NOUN'
lemma = lemmatizer.lemmatize(t)[0]
print(lemma)

t2 = nlp('blazing')[0]
t2.pos_ = 'VERB'
lemma2 = lemmatizer.lemmatize(t2)[0]
print(lemma2)

t3 = nlp('fastest')[0]
t3.pos_ = 'ADJ'
lemma3 = lemmatizer.lemmatize(t3)[0]
print(lemma3)