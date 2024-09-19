#Practical 9
# write a program to implemtent dependency parsing of a given text

import spacy
from spacy import displacy

# Load the pre-trained English model 
nlp = spacy.load('en_core_web_sm')

# Example sentence 
sentence = 'The dog saw the cat in the park'

# Parse the sentence 
doc = nlp(sentence)

# Print the syntactic dependency information 
for token in doc:
    print(f'{token.text:<12} {token.dep_:<10} {token.head.text}')

# Visualize the parse tree using displacy 
displacy.serve(doc, style="dep")
