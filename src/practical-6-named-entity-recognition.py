# Practical no 6
# writing a program to Implement Named Entity Recognition

import spacy
nlp = spacy.load('en_core_web_sm') # when it will throw some error like Can't find model 'en_core_web_sm'. It doesn't seem to be a Python package or a valid path to a data directory. 

#run this then
# !python -m spacy download en 

content = "Congrees leaders are giving us dream just like when we will put potato in the machine then we will get gold in back"
doc = nlp(content)

for ent in doc.ents:
    print(ent.text,
          ent.start_char,
          ent.end_char,
          ent.label)

#visualize
from spacy import displacy
displacy.render(doc, style="ent")

#creating datagram from the named entities extracted by spacy
import pandas as pd
entities = [
    (ent.text, ent.label_, ent.lemma_) for ent in doc.ents
]

df = pd.DataFrame(entities, columns=["text", "type" , "lemma"])
print(df)