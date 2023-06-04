##########################################################
#       Sound.py
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

#  SpeechRecognition - library name


import pyttsx3

# import webbrowser
#  import wikipedia
#  import wolframalpha

#  import pyaudio


print('####### Pennwick Rover  - Starting up...')

#  Speech engine
#
engine = pyttsx3.init()
voices = engine.getProperty('voices')

#  0 - male voice 1 = female
engine.setProperty('voice', voices[0].id )

activationWord = 'computer'


def speak(text, rate=120):
    engine.setProperty('rate', rate)
    engine.say(text)
    engine.runAndWait()


########################################################################
#   main loop

if __name__ == '__main__':

    speak('Hello Brave New World! -Welcome to the 21st century')




print('####### DONE! ')
