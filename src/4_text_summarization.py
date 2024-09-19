
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize,sent_tokenize
nltk.download('stopwords')
nltk.download('punkt')

text=""" Text summarization is the process of generating short,
luent, and most importantly accurate summary of a respectively longer text document.
The main idea behind automatic text summarization is to be able to find a short
subset of the most essential information from the entire set and present it in
a human-readable format. As online textual data grows, automatic text summarization
methods have the potential to be very helpful because more useful information
can be read in a short time.
"""

stopwords=set(stopwords.words("english"))
print(stopwords)
words=word_tokenize(text)
print(words)



freqTable=dict()
for word in words:
  word=word.lower()
  if word in stopwords:
    continue
  if word in freqTable:
    freqTable[word]+=1
  else:
    freqTable[word]=1
print(freqTable)



sentences=sent_tokenize(text)
print(sentences)
sentenceValue=dict()

for sentence in sentences:
  for word,freq in freqTable.items():
    #print(word,freq)
    if word in sentence.lower():
      if sentence in sentenceValue:
        sentenceValue[sentence]+=freq
      else:
        sentenceValue[sentence]=freq
print(sentenceValue)
sumValues=0
for sentence in sentenceValue:
  sumValues+=sentenceValue[sentence]
print(sumValues)

average=int(sumValues/len(sentenceValue))
print(average)
summary=''
for sentence in sentences:
  if(sentence in sentenceValue) and (sentenceValue[sentence] > (1.2 * average)):
    summary+= '' + sentence
print(summary)
