import spacy

nlp = spacy.load('en_core_web_sm')  # carrega o modelo en (english) do spacy em um objeto python

my_string1 = u'AC/DC are the best band '
my_string2 = u"AC/DC come and take over the city"

doc1 = nlp(my_string1)
for ent in doc1.ents:
    print(ent.text, ent.label_)

doc2 = nlp(my_string2)
for ent in doc2.ents:
    print(ent.text, ent.label_)
