# Practical no 5
# writing the program to implement a n-gram model


from nltk.util import ngrams

# Unigram or 1-gram
n=1
sentence = "Python is awesome and very easy to write there you only need logic to write"
Unigrams = ngrams(sentence.split(),n)
print("---Unigram---")
for item in Unigrams:
    print(item)
print()

# Bigram or 2-gram
n=2
sentence = "Python is awesome and very easy to write there you only need logic to write"
Bigrams = ngrams(sentence.split(),n)
print("---Bigram---")
for item2 in Bigrams:
    print(item2)
print()

# Trigram or 3-gram
n=3
sentence = "Python is awesome and very easy to write there you only need logic to write"
Trigram = ngrams(sentence.split(),n)
print("---Trigram---")
for item3 in Trigram:
    print(item3)
print()

# Everygram 
# This offers us that how many words we have given on the basis of it. it give us output for example you can prefer program that is down of it 

from nltk.util import everygrams

text = "python is awesome and very easy to write"
text_split = text.split()

everygram_text = list(everygrams(text_split))
final_everygram_lst = []
for i in everygram_text:
    print(i)