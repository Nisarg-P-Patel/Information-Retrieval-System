# -*- coding: utf-8 -*-
"""Text Classification with Naive Bayes.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1S8JqI4gVSk8cyjHEE9psWXkN7tVDHPr3

# AIM :- Text Classification using naive Bayesian approach.

# Importing necessary libraries
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

df = pd.read_csv('spam.csv', encoding='latin-1')[['v1', 'v2']]
df.columns = ['label', 'message']
df.head()

df.groupby('label').describe()

"""# Visualization of dataset"""

sns.countplot(data=df, x='label')

"""# Pre-processing"""

def toLower(sentence):
    return sentence.lower()

def tokenizer(sentence):
    tokens = list(set(nltk.word_tokenize(sentence)))
    return tokens

def stopwords_removal(tokens):
    stop_words = nltk.corpus.stopwords.words('english')
    stop_words.extend([',','?','""',"''",'.','!', "'",'"',"'d","'ll",'[',']','--',':',';','///','@', '``',
                       '#', '$', '%', '&', "'re", "'s", '(', ')', '*', '**', '**the', '-', '/', '//',
                       '§', '§§','...','–', '—', '‘', '’', '“', '”', '•', '─',"'m", "'ve", '***'])
    filtered_tokens = [i for i in tokens if not i in stop_words]
    return filtered_tokens

def stemming(tokens):
    stemmer = nltk.stem.porter.PorterStemmer()
    stemmed_tokens = [stemmer.stem(i) for i in tokens]
    return stemmed_tokens

def pre_process(text):
    tokens = [word for sent in nltk.sent_tokenize(text) for word in nltk.word_tokenize(sent)]
    tokens = stopwords_removal(tokens)
    stems = stemming(tokens)
    return stems

df['message'][:15].apply(pre_process)

"""# Creating Tf-idf Vectorizer"""

tfidfv = TfidfVectorizer(analyzer=pre_process)
data = tfidfv.fit_transform(df['message'])

mess = df.iloc[2]['message']
print(mess)

print(tfidfv.transform([mess]))

"""# Creating pipeline for model (Vetorizer+MultinomialNB)"""

spam_filter = Pipeline([
    ('vectorizer', TfidfVectorizer(analyzer=pre_process)), # messages to weighted TFIDF score
    ('classifier', MultinomialNB())                    # train on TFIDF vectors with Naive Bayes
])

x_train, x_test, y_train, y_test = train_test_split(df['message'], df['label'], test_size=0.25, random_state = 21)

spam_filter.fit(x_train, y_train)

predictions = spam_filter.predict(x_test)

count = 0
for i in range(len(y_test)):
    if y_test.iloc[i] != predictions[i]:
        count += 1
print('Total number of test cases', len(y_test))
print('Number of wrong of predictions', count)

"""# Result Evaluation"""

print(classification_report(predictions, y_test))

"""# For custom input"""

def detect_spam(s):
    return spam_filter.predict([s])[0]

x = input('Enter message for classification in spam/non-spam\n')
detect_spam(x)

"""# Learning Outcomes

1. I got to learn how naive bayes works with text data and it relation with previous input.
    2. I got to learn how to create pipeline for model which directly do all the necessary things.
    3. I got to leran different types of metrics like macro avg. and weighted avg.
"""

