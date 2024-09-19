import nltk
nltk.download("punkt")
nltk.download("averaged_perceptron_tagger")
from nltk.tokenize import word_tokenize
from nltk import pos_tag
text = "nltk is powerfull library for natural language processing"
words = word_tokenize(text)
pos_tags = pos_tag(words)
print("original text")
print(text)
print("\n pos tagging result: ")
for word,pos_tag in pos_tags:
    print(f"{word}:{pos_tag}")

def editdistance(str1, str2, m,n):
    if m==0:
        return n 
    if n==0:
        return m
    if str1[m-1] == str2[n-1]:
        return editdistance(str1 , str2 , m-1 , n-1)
    return 1+min(editdistance(str1 , str2, m, n-1),
                 editdistance(str1, str2, m-1,n),
                 editdistance(str1, str2, m-1, n-1))
str1= "sunday"
str2= "saturday"
print(editdistance(str1, str2,len(str1), len(str2)))
