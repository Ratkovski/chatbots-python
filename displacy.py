import spacy
from spacy import displacy

nlp = spacy.load('en_core_web_sm')
# doc = nlp(u'Book a table at the restaurant and the taxi to the hotel')
# displacy.serve(doc, style='dep')
#
# # http://localhost:5000/
# # visualização do parsing de dependencias

doc2 = nlp(u'What are some places to visit in Berlin and stay in Lubeck')
places = [doc2[7], doc2[11]]
actions = [doc2[5], doc2[9]]


for place in places:
    for tok in place.ancestors:
        if tok in actions:
            print("User is referring {} to {}".format(place,tok))
            break