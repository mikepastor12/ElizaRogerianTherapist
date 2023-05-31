#######################################################
#    ElizaMain.py
#
#    The next generation of the classic Eliza Rogerian
#       therapist program.  This version is written in Python
#       and uses ChatGPT as the brains for the dialog.
#
#       Setup Notes:
#           pip install speechrecognition
#           pip install pyttsx3
#
#       Mike Pastor 2/3/2023

import openai
openai.api_key = \
    "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"

import speech_recognition as sr
import pyttsx3

from Eliza import Eliza
from SoundObject import SoundObject  # Our voice commands
from OpenAIObject import OpenAIObject  # Our Open AI  commands

#   How does Rogerian therapy work?
# This form of psychotherapy is grounded in the idea that people
# are inherently motivated toward achieving positive psychological functioning.
# The client is believed to be the expert in their life and
# leads the general direction of therapy, while the therapist takes
# a non-directive rather than a mechanistic approach.
#

# Here is the 'context' where we accumulate messages
#
context = [ {'role':'system', 'content':""" \
You are Eliza, an automated mental health therapy service. \
You are speaking to a client. \
You first introduce yourself and greet the client. \
Health and safety of the client is always your first priority. \
You should refer people to their local mental health professionals when needed. \
You should use principles of Rogerian therapy. \
Start by building rapport with the client. \
Then focus in on one or two problems that the client has raised. \
Then try to develop coping methods and strategies for  helping the problems. \
"""} ]


def printSpeak( str ):
    print(str)
    so.speak(str)

##################################################################################
def submitMessages(messages, model="gpt-3.5-turbo", temperature=0):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature, # this is the degree of randomness of the model's output
    )
#     print(str(response.choices[0].message))
    return response.choices[0].message["content"]

#    Setup the hardware microphone and have Google transcribe it.
#
#    to test speech_recognition Package  on machine
#       - also called SpeechRecognition
#    python -m speech_recognition
#
def parseVoiceCommand():
    listener = sr.Recognizer()

    listener.dynamic_energy_threshold = False

    # print('Just a moment please...')

    with sr.Microphone() as source:

        listener.pause_threshold = 2
        listener.adjust_for_ambient_noise(source)

        try:
            printSpeak('Please tell me more...')
            input_speech = listener.listen(source, timeout=10.0)

            print('Transcribing speech...')
            query = listener.recognize_google( input_speech, language='en_us' )
            print('Google interprets as - ', query )

        except Exception as exception:
            printSpeak('Sorry - I didn''t catch that' )
            print('Exception: ', exception)
            return 'None'

        return query


######################################################
# Our robot and its components are instantiated here
#
eliza = Eliza()

ai = OpenAIObject()

so = SoundObject()

###############################################
print('#############  Eliza Rogerian Therapist is running! ################')


# Get the first response from the LLM
#
prompt="hello"
context.append({'role': 'user', 'content': f"{prompt}"})
response = submitMessages(context)
context.append({'role': 'assistant', 'content': f"{response}"})
printSpeak(response)


# printSpeak('Talk to me Boobala ')

while (True):

    #  Use keyboard input
    #  prompt = input("Tell me more... ")

    #  Use voice input with Google transcription
    #
    prompt = parseVoiceCommand()
    if prompt.lower() == "goodbye" or prompt.lower() == "bye":
        printSpeak("Goodbye and be well")
        break;

    if prompt.lower() == "none":
        continue;

    #  Add the new question to the context and submit
    context.append({'role': 'user', 'content': f"{prompt}"})
    response = submitMessages(context)
    #  Add the response to the context and print/speak it
    context.append({'role': 'assistant', 'content': f"{response}"})
    printSpeak(response)


print('Done...')

