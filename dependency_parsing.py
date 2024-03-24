import spacy

# Example 1
nlp = spacy.load('en_core_web_sm')  # carrega o modelo en (english) do spacy em um objeto python
doc = nlp(u'Book me a flight from Bangalore to Goa')
blr, goa = doc[5], doc[7]
print(list(blr.ancestors))
print(list(goa.ancestors))

"""
ancestrais são o token que fica mais á direita entre os descendentes sintaticos desse token
"""

print(list(doc[4].ancestors))

# verificar programaticamente se um item do objeto doc é ancestral de outro item desse objeto

print(doc[3].is_ancestor(doc[5]))

# Example 2

doc2 = nlp(u'Book a table at the restaurant and the taxi to the hotel')
print(list(doc2[3].children))
tasks = doc2[2], doc2[8]  # table, taxi
tasks_target = doc2[5], doc2[11]  # restaurante , hotel

for task in tasks_target:
    for tok in task.ancestors:
        if tok in tasks:
            print("Booking of {} belongs to {}".format(tok, task))





