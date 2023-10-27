import random, json, pickle, numpy as np, tensorflow as tf, nltk
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()
intents = json.loads(open('intents.json').read())

words = []
classes = []
documents = []
ignoreLetters = ['!', '?','<', '.', ',']

for intent in intents['intents']:
    for pattern in intent['patterns']