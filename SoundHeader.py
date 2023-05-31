##############################################################
#   SoundHeader.py
#
#   A Class to incorporate voice commands into a program
#
#   Mike Pastor 2/1/2023


from datetime import datetime

import speech_recognition as sr

import pyttsx3


print('####### Pennwick Rover  - Starting up...')

#  Speech engine
#
engine = pyttsx3.init()
voices = engine.getProperty('voices')

#  0 - male voice 1 = female
engine.setProperty('voice', voices[1].id )

activationWord = 'eliza'

def speak(text, rate=120):
    engine.setProperty('rate', rate)
    engine.say(text)
    engine.runAndWait()


def parseCommand():
    listener = sr.Recognizer()

    listener.dynamic_energy_threshold = False

    print('Listening...')

    with sr.Microphone() as source:

        listener.pause_threshold = 2
        print('How can I help you? ')
        input_speech = listener.listen(source )
        # , timeout=10.0

        try:
            print('Recognizing speech...')
            query = listener.recognize_google( input_speech, language='en_us' )
            print('Google interprets as - ', query )
        except Exception as exception:
            print('Sorry - didn''t catch that' )
            speak('Sorry Michael - didn''t catch that')
            print(exception)
            return 'None'

        return query



