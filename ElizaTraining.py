###################################################
#       ElizaTraining.py
#
#       Michael Pastor 2/1/2023

import random
import json
import pickle
import numpy as np

import nltk
from nltk.stem import WordNetLemmatizer
nltk.download('punkt')
nltk.download('wordnet')

#  work, working, worked works --> work

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Dropout
from tensorflow.keras.optimizers import SGD

lemmatizer = WordNetLemmatizer()

elizaIntents = json.loads( open('ElizaIntents.json').read() )
print( 'intents = ', elizaIntents )

words = []
classes = []
documents = []
ignore_letters = ['?', '!', '.', ',']

for intent in elizaIntents['elizaintents']:
    for pattern in intent['patterns']:
        word_list = nltk.word_tokenize( pattern )
        words.extend( word_list )
        documents.append( (word_list, intent['tag']) )
        if intent['tag'] not in classes:
            classes.append(intent['tag'])


words = [ lemmatizer.lemmatize( word ) for word in words if word not in ignore_letters ]
#  sort and remove duplicates
words = sorted( set( words ) )

classes = sorted( set(classes) )

pickle.dump( words, open( 'words.pkl', 'wb' ))
pickle.dump( classes, open( 'classes.pkl', 'wb' ))

# bag of words
training = []
output_empty = [0] * len(classes)

for document in documents:
    bag = []
    word_patterns = document[0]
    word_patterns = [ lemmatizer.lemmatize(word.lower()) for word in word_patterns]

    for word in words:
        bag.append(1) if word in word_patterns else bag.append(0)

    output_row = list( output_empty )
    output_row[classes.index(document[1])] = 1
    training.append([bag, output_row])

random.shuffle( training )
training = np.array( training )

train_x = list( training[:, 0])
train_y = list( training[:, 1])

print( training )

#  Build the model
#
model = Sequential()
# rectified linear unit  - relu
model.add( Dense(128, input_shape=( len(train_x[0]),), activation='relu') )
model.add( Dropout(0.5))
model.add( Dense( 64, activation='relu' ))
model.add( Dropout(0.5) )
model.add( Dense( len(train_y[0]), activation='softmax'))

sgd = SGD( lr=0.01, decay=1e-6, momentum=0.9, nesterov=True )
model.compile( loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'] )

hist = model.fit( np.array( train_x ), np.array( train_y ), epochs=200, batch_size=5, verbose=1)

model.save( 'Eliza_model.h5', hist)

print( 'Done...')







