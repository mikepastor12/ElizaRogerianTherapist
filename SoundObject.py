##########################################################
#       SoundObject.py
#
#       Give our Robots speech capabilities
#
#       pip install speechrecognition
#       pip install pyttsx3
#           pip install pyaudio

#       Mike Pastor - June 5, 2023

import speech_recognition as sr
import pyttsx3
#  import pyaudio

class SoundObject():

    print('########### Eliza  SoundObject  Initialized #############')
    #  Speech engine
    #
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')

    #  0 - male voice 1 = female
    engine.setProperty('voice', voices[1].id )
    activationWord = 'computer'

    #######################################
    #   Speak at the set rate
    def speak(self, text, rate=120):
        self.engine.setProperty('rate', rate)
        self.engine.say(text)
        self.engine.runAndWait()

    #####################################
    #  Print and speak the string
    def printSpeak(self, str, rate=160):
        print(str)
        self.speak(str, rate)


    ####################################################################
    #     Setup the hardware microphone
    #       and have Google transcribe the input
    #
    #     to test speech_recognition Package  on machine
    #       - Package is also called SpeechRecognition
    #       python -m speech_recognition
    #
    def parseVoiceCommand2(self):

        listener = sr.Recognizer()

        listener.dynamic_energy_threshold = False

        print('...')

        with sr.Microphone() as source:

            listener.pause_threshold = 1
            listener.adjust_for_ambient_noise(source)

            try:
                self.printSpeak('Please tell me more...')
                input_speech = listener.listen(source, timeout=60.0)
                # input_speech = listener.listen(source)

                print('Transcribing speech...')
                query = listener.recognize_google(input_speech, language='en_us')
                print('Google interprets as - ', query)

            except Exception as exception:
                self.printSpeak('Sorry - I didn''t catch that')
                print('Exception: ', exception)
                if exception == "KeyboardInterrupt":
                    exit(-1)
                return 'None'

            return query


########################################################################
#   Quick test
#
# if __name__ == '__main__':
#
#     speak('Hello Brave New World! -Welcome to the 21st century')
#     print('####### DONE! ')
