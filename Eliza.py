#####################################################
#       Eliza.py
#
#       Build the next generation of the famous Eliza program.
#       Eliza simulates a Rogerian Therapist with basic reflections.
#       Eliza was one of the first AI programs introduced in the 1960s.
#       I implemented a version of Eliza using C language in early 1990s
#           and build on some of those ideas here...
#
#       Michael Pastor - January 31, 2023

from Robot import Robot
import SoundHeader as sh   # Our voice commands

import random
import json
import pickle
import numpy as np

import nltk
from nltk.stem import WordNetLemmatizer
nltk.download('punkt')
nltk.download('wordnet')

from tensorflow.keras.models import load_model



class Eliza( Robot ):

    lemmatizer = WordNetLemmatizer()

    # Load intents
    elizaIntents = json.loads( open('ElizaIntents.json').read() )
    print( 'intents = ', elizaIntents )

    # Load words and classes from PICKLE files
    words = pickle.load( open('words.pkl', 'rb' ))
    classes = pickle.load( open('classes.pkl', 'rb' ))
    print( 'words = ', type(words) )

    model = load_model( 'Eliza_model.h5')

    def __init__(self):

        super(Eliza, self).__init__()  # All features from parent class

        # Ensure that all features get stopped on exit
        #
        print("############ Eliza - Sub Robot Initialized ##########")


    def clean_up_sentence( self, sentence ):
        sentence_words = nltk.word_tokenize( sentence )
        sentence_words = [self.lemmatizer.lemmatize(word) for word in sentence_words]
        return sentence_words

    def bag_of_words( self, sentence):
        sentence_words = self.clean_up_sentence(sentence)
        bag = [0] * len( self.words )
        for w in sentence_words:
            for i, word in enumerate(self.words):
                if word == w:
                    bag[i] = 1

        return np.array(bag)

    def predict_class( self, sentence):
        bow = self.bag_of_words( sentence )

        # predict the response from query sentence
        #
        pred1 = self.model.predict( np.array( [bow] ))[0]
        ERROR_THRESHOLD = 0.25
        results = [ [i, r] for i, r in enumerate(pred1) if r > ERROR_THRESHOLD ]

        results.sort( key=lambda x: x[1], reverse=True )

        return_list = []

        for r in results:
            return_list.append( {'intent': self.classes[ r[0] ], 'probability': str( r[1] )}  )

        return return_list

    def get_response(  self, intents_list, intents_json ):

        tag = intents_list[0]['intent']  # Highest scoring intent
        print( 'PRED INTENT --> ', tag )

        list_of_intents = intents_json['elizaintents']
        for i in list_of_intents:
            if i['tag'] == tag:
                result = random.choice( i['responses'])
                break;

        return result, tag

