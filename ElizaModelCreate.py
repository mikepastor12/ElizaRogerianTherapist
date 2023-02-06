###################################################
#       ElizaModelCreate.py
#
#       This code creates the Tensorflow Keras Sequential
#           Neural Network model
#           and writes the 'Eliza_model.h5' model file.
#
#       Michael Pastor 2/5/2023

import pandas as pd
import numpy as np
import random
import json
import pickle

import nltk
from nltk.stem import WordNetLemmatizer
nltk.download('punkt')
nltk.download('wordnet')

#  work, working, worked works --> work

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Dropout
from tensorflow.keras.optimizers import SGD

# Some parameters
#
TRAINING_EPOCHS = 200
MODEL_FILENAME='Eliza_model.h5'

#  Get the stem meaning of word
#
lemmatizer = WordNetLemmatizer()


#################################
#   Load the Intents database
#
elizaIntents = json.loads( open('ElizaIntents.json').read() )
print( 'intents = ', elizaIntents )

elizaIntents_csv = pd.read_csv('IntentsDatabase.csv', usecols = ['intent_name','intent_examples','intent_responses'] )
#
# elizaIntents_csv = csv.DictReader(elizaIntents_csvraw)
elizaIntents_df = pd.DataFrame( elizaIntents_csv )
elizaIntents_df.reset_index()
print('INTENTS \n', elizaIntents_df )

words = []
classes = []
documents = []
ignore_letters = ['?', '!', '.', ',']

elizaIntents_df.reset_index()
for index, myIntent in elizaIntents_df.iterrows():

    print( myIntent['intent_name'] )
    print(myIntent['intent_examples'])
    examples = myIntent['intent_examples'].replace('"', '')
    myExamples = examples.split(',')
    for example in myExamples:
        example_list = nltk.word_tokenize(example)
        words.extend( example_list )
        documents.append((example_list, myIntent['intent_name']))
        if myIntent['intent_name'] not in classes:
            classes.append(myIntent['intent_name'])

print('#################################   done ## ', words)

#
# for intent in elizaIntents['elizaintents']:
#     for pattern in intent['patterns']:
#         word_list = nltk.word_tokenize( pattern )
#         words.extend( word_list )
#         documents.append( (word_list, intent['tag']) )
#         if intent['tag'] not in classes:
#             classes.append(intent['tag'])
#
# print('####   orig ## ', words)


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

# print( training )

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

print( 'Ready for Training ...',TRAINING_EPOCHS)
hist = model.fit( np.array( train_x ), np.array( train_y ), epochs=TRAINING_EPOCHS, batch_size=5, verbose=1)


model.save( MODEL_FILENAME, hist)

print( 'Done - Model file is written ', MODEL_FILENAME)







