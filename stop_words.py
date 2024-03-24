import spacy
from spacy.lang.en.stop_words import STOP_WORDS

"""
Stop words são uma parte muito importantena limpeza de texto, elas ajudam na remoção de dados irrelenvantes
antes de tentarmos executar o  processamento parta dar sentido ao texto.
"""
#list stop words in english
print(STOP_WORDS)
nlp = spacy.load('en_core_web_sm')

#verify stop words
print(nlp.vocab[u'is'].is_stop)
print(nlp.vocab[u'hello'].is_stop)
