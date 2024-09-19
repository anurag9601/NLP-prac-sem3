#practical 8
# writing a program to implement syntactic parsing of a give text
import nltk
from nltk import CFG 
from nltk.parse import ChartParser 

#Defining a simple context-free grammer
grammer = CFG.fromstring("""
                         S -> NP VP
                         NP -> Det N | Det N PP
                         PP -> P NP
                         VP -> V NP | V NP PP
                         Det -> 'the' | a
                         N -> 'dog' | 'cat' | 'park' | 'telescope'
                         V -> 'saw' | 'ate' 
                         P -> 'in' | 'on' | 'with'
                         """)

# create a parser with the defined grammer 
parser = ChartParser(grammer)

# Example sentence 
sentence = 'the dog saw the cat in the park'.split()

#Parse the sentence
for tree in parser.parse(sentence):
    print(tree)
    tree.pretty_print()