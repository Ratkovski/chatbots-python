import spacy

# Exemplo 1

nlp = spacy.load('en_core_web_sm')  # carrega o modelo en (english) do spacy em um objeto python
doc = nlp(u'I am learning how to build chatboats')  # cria um objeto doc
for token in doc:
    print(token.text, token.pos_)  # exibe o texto e a  POS

# Exemplo 2

doc2 = nlp(u'I am going to London next week for a meeting')
for token in doc2:
    print(token.text, token.pos_)

# Exemplo 3

doc3 = nlp(u'Google release "Move Mirror" Ai Experiment that mactches your pose from 80,000 images')
for token in doc3:
    print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_, token.shape_, token.is_alpha, token.is_stop)

# Exemplo 4

doc4 = nlp(u'I am learning how to build chatboats')
for token in doc4:
    print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_, token.shape_, token.is_alpha, token.is_stop)


