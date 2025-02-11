# Tri-gram model to predict next word probability
import nltk
nltk.download('reuters')
nltk.download('punkt')
from nltk.corpus import reuters
from nltk import bigrams, trigrams
from collections import Counter, defaultdict

# create a placeholder for model
model = defaultdict(lambda: defaultdict(lambda: 0))

# count frequency of co-occurance
for sentence in reuters.sents():
    for w1, w2, w3 in trigrams(sentence, pad_right=True, pad_left=True):
        model[(w1,w2)][w3] += 1

# Let's transform the couts to probabilities
for w1_w2 in model:
    total_count = float(sum(model[w1_w2].values()))
    for w3 in model[w1_w2]:
        model[w1_w2][w3] /= total_count
    
sorted(dict(model["the","news"]).items(), key=lambda x:-1*x[1])
