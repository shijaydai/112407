import pandas as pd
import os
import re
import numpy as np

for dirname, _, filenames in os.walk('/Users/asus-fa506/archive'):
    for filename in filenames:
        print(os.path.join(dirname, filename))
        
spam_dataframe = pd.read_csv('/Users/Lenovo/Desktop/word/Gappdj_en.csv')
spam_dataframe

spam_probability = len(spam_dataframe[spam_dataframe['effflag'] == 1]) / len(spam_dataframe)
ham_probability = len(spam_dataframe[spam_dataframe['effflag'] == 0]) / len(spam_dataframe)

print('Spam Probability: ', spam_probability)
print('Ham Probability: ', ham_probability)

from sklearn.feature_extraction.text import CountVectorizer
vectorizer=CountVectorizer()
spamham_countVectorizer=vectorizer.fit_transform(spam_dataframe['text'])

label=spam_dataframe['effflag']
X=spamham_countVectorizer
y=label

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)

from sklearn.naive_bayes import MultinomialNB

NB_classifier=MultinomialNB()
NB_classifier.fit(X_train,y_train)

y_predict_test=NB_classifier.predict(X_test)
y_predict_test

from sklearn.metrics import classification_report

print(classification_report(y_test,y_predict_test))

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    tokens = text.split()
    return ' '.join(tokens)

def build_vocabulary(texts):
    vocabulary = set()
    for text in texts:
        tokens = text.split()
        vocabulary.update(tokens)
    return list(vocabulary)

def create_bow(texts, vocabulary):
    bow_matrix = []
    for text in texts:
        tokens = text.split()
        bow_vector = [tokens.count(word) for word in vocabulary]
        bow_matrix.append(bow_vector)
    return bow_matrix

preprocessed_texts = [preprocess_text(text) for text in spam_dataframe['text']]

# Build vocabulary
vocabulary = build_vocabulary(preprocessed_texts)

# Create Bag of Words (BoW) representation
bow_matrix = create_bow(preprocessed_texts, vocabulary)

# Convert bow_matrix to a NumPy array
X = np.array(bow_matrix)
y = np.array(spam_dataframe['effflag'])

X_train = X[:int(len(X) * 0.8)]
X_test = X[int(len(X) * 0.8):]
y_train = y[:int(len(y) * 0.8)]
y_test = y[int(len(y) * 0.8):]

class CustomMultinomialNB:
    def __init__(self, alpha=1):
        self.alpha = alpha

    def fit(self, X, y):
        self.X = X
        self.y = y
        self.classes = np.unique(y)
        self.parameters = {}
        for i, c in enumerate(self.classes):
            X_c = X[np.where(y == c)]
            self.parameters["phi_" + str(c)] = len(X_c) / len(X)
            self.parameters["theta_" + str(c)] = (X_c.sum(axis=0) + self.alpha) / (np.sum(X_c.sum(axis=0) + self.alpha))

    def predict(self, X):
        predictions = []
        for x in X:
            phi_list = []
            for i, c in enumerate(self.classes):
                phi = np.log(self.parameters["phi_" + str(c)])
                theta = np.sum(np.log(self.parameters["theta_" + str(c)]) * x)
                phi_list.append(phi + theta)
            predictions.append(self.classes[np.argmax(phi_list)])
        return predictions
    
NB_classifier=CustomMultinomialNB()
NB_classifier.fit(X_train,y_train)

y_predict_test=NB_classifier.predict(X_test)

print('Accuracy: ', np.sum(y_predict_test == y_test) / len(y_test))