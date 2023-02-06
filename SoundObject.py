##########################################################
#       SoundObject.py
#
#
#       pip install speechrecognition
#       pip install pyttsx3
#
#           pip install wikipedia
#           pip install wolframalpha
#           pip install pyaudio

#     sudo apt install espeak
#      sudo apt install portaudio19-dev python3-pyaudio

#       speaker-test -c2 -twav -l7

#       Mike Pastor - January 27, 2023


from datetime import datetime

import speech_recognition as sr


import pyttsx3

# import webbrowser
#  import wikipedia
#  import wolframalpha

#  import pyaudio

class SoundObject():

    print('####### Pennwick Rover  - Starting up...')
    #  Speech engine
    #
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')

    #  0 - male voice 1 = female
    engine.setProperty('voice', voices[1].id )

    activationWord = 'computer'


    def speak(self, text, rate=120):
        self.engine.setProperty('rate', rate)
        self.engine.say(text)
        self.engine.runAndWait()

    def parseCommand(self):
        listener = sr.Recognizer()

        listener.dynamic_energy_threshold = False

        print('Listening...')

        with sr.Microphone() as source:

            listener.pause_threshold = 2
            print('How can I help you? ')
            input_speech = listener.listen(source)
            # , timeout=10.0

            try:
                print('Recognizing speech...')
                query = listener.recognize_google(input_speech, language='en_us')
                print('Google interprets as - ', query)
            except Exception as exception:
                print('Sorry - didn''t catch that')
                self.speak('Sorry Michael - didn''t catch that')
                print(exception)
                return 'None'

            return query

########################################################################
#   main loop
#
# if __name__ == '__main__':
#
#     speak('Hello Brave New World! -Welcome to the 21st century')
#     print('####### DONE! ')
