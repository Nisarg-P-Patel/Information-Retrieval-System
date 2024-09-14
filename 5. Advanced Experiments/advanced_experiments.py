# -*- coding: utf-8 -*-
"""Advanced Experiments.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1xw2gn0yYg1AdzM02ZbbgG3chFvWLE2Z3

# AIM :- Exploring Virtual Labs for advanced experiments.

1.Check this link and complete Practical 4 (mandatory) and any other practical from that list.
    2.Prepare a presentation of maximum 10 slides based on your understanding on these two practicals.
    3.You may explore other resources from Internet if needed.
    4.Everyone will be individually evaluated based on one to one interaction.

# Packages Used
"""

import pandas as pd
import nltk
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

"""# Fetching data in document"""

document = ["One Two Six Four Three EOS EOS Two Six One Five Six One EOS Three Six Four Five Six EOS Six Five Four Three Six Two EOS Five Two Three Two Three EOS EOS Two Five Three One Two One EOS"]

# document = [ 'You book a flight eos I read a book eos You read eos']

"""# Pre-Processing of raw data"""

def toLower(sentence):
    return sentence.lower()

def tokenizer(sentence):
    tokens = list(set(nltk.word_tokenize(sentence)))
    return tokens

def stopwords_removal(tokens):
    stop_words = nltk.corpus.stopwords.words('english')
    stop_words.extend([',','?','""',"''",'.','!', "'",'"',"'d","'ll",'[',']','--',':',';','///'])
    filtered_tokens = [i for i in tokens if not i in stop_words]
    return filtered_tokens

def stemming(tokens):
    stemmer = nltk.stem.porter.PorterStemmer()
    stemmed_tokens = [stemmer.stem(i) for i in tokens]
    return stemmed_tokens

def pre_process(text):
    tokens = [word for sent in nltk.sent_tokenize(text) for word in nltk.word_tokenize(sent)]
#     tokens = stopwords_removal(tokens)
    stems = stemming(tokens)
    return stems

"""# Finding bigram probablity of the document without smooting"""

#define vectorizer parameters
tfidf_vectorizer = TfidfVectorizer(
    use_idf=True,tokenizer=pre_process,
    smooth_idf=False,
    ngram_range=(2,2))

tfidf_matrix = tfidf_vectorizer.fit_transform(document) #fit the vectorizer to synopses

print(tfidf_matrix.shape)

df = pd.DataFrame(tfidf_matrix.toarray(),columns=tfidf_vectorizer.get_feature_names())
df

"""# Defining function for counting probablity of input sentence according to corpus"""

def prob():
    input_sequence = input()
    input_sequence = pre_process(input_sequence)
    print(input_sequence)
    prob = 1
    for x in range(len(input_sequence)-1):
        temp="".join(input_sequence[x])+" "+"".join(input_sequence[x+1])
        if temp in tfidf_vectorizer.get_feature_names():
            prob*=df.loc[:,temp]
        else:
            prob=0
            print(temp,' is not a feature of vocab sequence.')
            break
    print(float(prob))

prob()

"""# Finding bigram probablity of the document with smooting"""

#define vectorizer parameters
tfidf_vectorizer = TfidfVectorizer(
    use_idf=True,tokenizer=pre_process,
    smooth_idf=True,
    ngram_range=(2,2))

tfidf_matrix = tfidf_vectorizer.fit_transform(document) #fit the vectorizer to synopses

print(tfidf_matrix.shape)

df = pd.DataFrame(tfidf_matrix.toarray(),columns=tfidf_vectorizer.get_feature_names())
df

prob()
