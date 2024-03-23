import spacy
nlp = spacy.load('') #carrega o modelo en (english) do spacy em um objeto python
doc = nlp(u'I am learning how to build chatboats')#cria um objeto doc
for token in doc:
    print(token.text, token.pos_) #exibe o texto e a  POS
