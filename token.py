import spacy

nlp = spacy.load('en_core_web_sm')  # carrega o modelo en (english) do spacy em um objeto python
doc = nlp(u'Brexit is the impeding withdraw of the U.K from the European Union')
for token in doc:
    print(token.text)
