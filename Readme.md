Consulte a tabela a seguir para saber o significado de cada atributo que eximos no código.


|TEXTO |                                         Texto ou palavra que está sendo processado                                          |
| :---:  | :---   |
|LEMMA|                                      Forma raiz da palavra que está sendo processada.                                       |
|POS|                                                  Parte de fala da palavra.                                                  |
|TAG| Expressa a parte da fala (por exemplo, VERB) e algumas informações morfológicas (por exemplo, que o verbo está no passado). |
|DEP|                                 Dependência sintática (isto é, a relação entre os tokens).                                  |
|SHAPE|                      Forma da palavra (por exemplo, letras maiúsculas, pontuação, formato de dígitos).                      |
|ALPHA|                                             O token é um caractere alfabético?.                                             |
|STOP|                                   A palavra é uma stopword ou faz parte de uma stop list?                                   |


### Siglas
| Sigla | Significado                 |
|:-----:|:----------------------------|
|  NLP  | Natural Language Processing |
|  NER  | Named-Entity Recognition    |

### Porque a marcação POS é necessária em chatbots?
 - Para reduzir a complexidade de criação de um texto que não possa ser ensinado ou que seja ensinado com pouca segurança.


### Stemização e lematização
 - idk

Os modelo treinados com o acervo OntoNotes 5 dão suporte aos tipos de entidades a seguir 

|                         TIPO                          | DESCRIÇÃO                                            |
|:-----------------------------------------------------:|:-----------------------------------------------------|
|                        PERSON                         | People, including fictional                          |
|                         NORP                          | Nationalities or religious or political groups       
|                       FACILITY                        | Buildings, airports, highways, bridges, etc.         |
|                     ORGANIZATION                      | Companies, agencies, institutions, etc.              |
|                          GPE                          | Countries, cities, states                            |
|                       LOCATION                        | Non-GPE locations, mountain ranges, bodies of water  |
|                        PRODUCT                        | Vehicles, weapons, foods, etc. (Not services)        |
|                         EVENT                         | Named hurricanes, battles, wars, sports events, etc. |
|                      WORK OF ART                      | Titles of books, songs, etc.                         |
|                          LAW                          | Named documents made into laws                       |
|                       LANGUAGE                        | Any named language                                   |
|                         DATE                          | Absolute or relative dates or periods                |
|                        PERCENT                        | Percentage (including “%”)                           |
|                         MONEY                         | Monetary values, including unit                      |
|                       QUANTITY                        | Measurements, as of weight or distance               |
|                        ORDINAL                        | “first”, “second”                                    |
| CARDINAL | Numerals that do not fall under another type         |

 
[OntoNotes Release 5.0](https://catalog.ldc.upenn.edu/docs/LDC2013T19/OntoNotes-Release-5.0.pdf)