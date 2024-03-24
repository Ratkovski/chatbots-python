import spacy

# Exemplo 1

"""
As entidades podem ser de diferentes tipos como uma pessoa,local, empresa
datas, numerais,etc. Elas podem ser acessadas por intermedio da
propriedade .ents do objeto doc.
"""

nlp = spacy.load('en_core_web_sm')  # carrega o modelo en (english) do spacy em um objeto python
my_string = nlp(
    u'Google has it headquarters in Mountain View, California having revenue amounted to 109.65 billion US dollars')

doc = nlp(my_string)

for ent in doc.ents:
    print(ent.text, ent.label_)

# Exemplo 2
my_string2 = nlp(
    u'Mark Zuckenberg born May 14, 1984 in New York is an American technology entrepreneur and philanthropist '
    u'best known for co-founding and leading Facebook as its chairman and CEO.')

doc2 = nlp(my_string2)

for ent in doc2.ents:
    print(ent.text, ent.label_)


# Exemplo 3
my_string3 = nlp(
    u'I usually wake up at 9:00 AM. 90% of my daytime goes in learning new things')

doc3 = nlp(my_string3)

for ent in doc3.ents:
    print(ent.text, ent.label_)
