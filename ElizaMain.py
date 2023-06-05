##############################################################################
#    ElizaMain.py
#
#    The next generation of the classic Eliza Rogerian
#       therapist program.  This version is written in Python
#       and uses ChatGPT as the brains for the dialog.
#
#       Setup Notes:
#           pip install openai
#           pip install speech_recognition
#           pip install pyttsx3, pyaudio
#
#       Mike Pastor 6/2/2023
import time

import openai
import speech_recognition as sr

from Eliza import Eliza
# from SoundObject import SoundObject  # Our voice commands
# from OpenAIObject import OpenAIObject  # Our Open AI  commands
# openai.api_key = Eliza.SK

################################################################################
#   Here is the 'context' where we
#    accumulate messages from the conversation
#
situationContext = [ {'role':'system', 'content':""" \
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


#  Print and speak the string
def printSpeak( str, rate=160 ):
    print(str)
    eliza.so.speak(str, rate)

#####################################################################
#  Submit the message list to OpenAI
#
def submitMessages(messages, model="gpt-3.5-turbo", temperature=0):
    #  print('messages:  ', messages)
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature
        # this is the degree of randomness of the model's output
    )

    #   print(str(response.choices[0].message))
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

    print('...')

    with sr.Microphone() as source:

        listener.pause_threshold = 1
        listener.adjust_for_ambient_noise(source)

        try:
            printSpeak('Please tell me more...')
            input_speech = listener.listen(source, timeout=60.0)
            # input_speech = listener.listen(source)

            print('Transcribing speech...')
            query = listener.recognize_google( input_speech, language='en_us' )
            print('Google interprets as - ', query )

        except Exception as exception:
            printSpeak('Sorry - I didn''t catch that' )
            print('Exception: ', exception)
            return 'None'

        return query


#######################################################################
# Our robot and its components are instantiated here
#
eliza = Eliza()

print('###############  Eliza Rogerian Therapist is ready ###################')


# Get the first response from the LLM
#
prompt="hello"
situationContext.append({'role': 'user', 'content': f"{prompt}"})
response = submitMessages(situationContext)
situationContext.append({'role': 'assistant', 'content': f"{response}"})
printSpeak(response)

# printSpeak('Talk to me Boobala ')

#  Loop thru the voice commands as they are received
#
while (True):

    #  Use keyboard input like this
    #  prompt = input("Tell me more... ")

    #  Use voice input with Google transcription
    #
    prompt = parseVoiceCommand()

    # Take care of Admin commands here
    if prompt.lower() == "goodbye" or prompt.lower() == "bye":
        printSpeak("Goodbye and be well")
        break;

    if prompt.lower() == "None":
        continue;

    if prompt.lower() == "please wait" or \
            prompt.lower() == "Eliza please wait" or \
            prompt.lower() == "pause":
        printSpeak('Waiting...')
        time.sleep( 600 ) # 10 minutes
        printSpeak("Shall we continue our session?")
        break;

    #  Add the new question to the situationContext and submit
    situationContext.append({'role': 'user', 'content': f"{prompt}"})
    response = submitMessages(situationContext)
    #  Add the response to the context and print/speak it
    situationContext.append({'role': 'assistant', 'content': f"{response}"})
    printSpeak(response)


print('Done...')

