#######################################################
#    ElizaMain-ChatGPT.py
#
#    Main loop for our robot.

#       Mike Pastor 2/5/2023

import pandas as pd
from Eliza import Eliza

from SoundObject import SoundObject  # Our voice commands
from OpenAIObject import OpenAIObject  # Our Open AI  commands

######################################################
# Our robot and its components are instantiated here
#
eliza = Eliza()

ai = OpenAIObject()

so = SoundObject()

###############################################
print('Eliza Rogerian Therapist is running!')

so.speak('Hello I am Eliza the Rogerian Therapist ')
#
# train_X = pd.read_csv('IntentsDatabase.csv')
#
# print( train_X)
#
# exit(0)

#
# while True:
#     # message = input("? ")
#     # parse as list
#     # query = sh.parseCommand().lower().split()
#     query = so.parseCommand().lower()
#
#     ints = eliza.predict_class( query )
#
#     res, tag = eliza.get_response(  ints, eliza.elizaIntents )
#     so.speak( res )
#
#     if tag == 'goodbye':
#         exit(0)


# OpenAI version
#
response = ai.do_completion("Act as a therapist")
so.speak( response )

while True:

    so.speak("tell me more...")
    query = so.parseCommand().lower()

    if query.lower() == 'goodbye':
        so.speak("Goodbye Michael - see you soon")
        exit(0)

    response = ai.do_completion( query )

    so.speak( response )

print('Done...')

