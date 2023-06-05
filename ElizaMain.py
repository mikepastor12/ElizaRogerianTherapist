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


################################################################################
#   Here is the 'context' where we
#    accumulate messages from the conversation
#
situationContext = [ {'role':'system', 'content':""" \
You are Eliza, an automated mental health therapy service. \
You are speaking to a client. \
You first introduce yourself and greet the client. \
Ask for the client's name and use it in the therapy. \
Health and safety of the client is always your first priority. \
You should refer people to their local mental health professionals when needed. \
You should use principles of Rogerian therapy. \
Start by building rapport with the client. \
Then focus in on one or two problems that the client has raised. \
Then try to develop coping methods and strategies for  helping the problems. \
"""} ]


#######################################################################
# Our Eliza Robot and its components are instantiated here
#
eliza = Eliza()

print('###############  Eliza Rogerian Therapist is ready ###################')


#######################################################################
# Prime the engine with the situationContext
#    and get the first response from the LLM
#
prompt="hello"
situationContext.append({'role': 'user', 'content': f"{prompt}"})
response = eliza.ai.submitMessages2(situationContext)
situationContext.append({'role': 'assistant', 'content': f"{response}"})
eliza.so.printSpeak(response)

#####################################################
#  Loop thru the voice commands as they are received
#
while (True):

    #  Use keyboard input like this
    #  prompt = input("Tell me more... ")

    #  Use voice input with Google transcription
    #
    prompt = eliza.so.parseVoiceCommand2()

    # Take care of Admin commands here
    if prompt.lower() == "goodbye" or prompt.lower() == "bye":
        eliza.so.printSpeak("Goodbye and be well")
        break;

    if prompt.lower() == "None":
        continue;

    if prompt.lower() == "please wait" or \
            prompt.lower() == "eliza please wait" or \
            prompt.lower() == "pause":
        eliza.so.printSpeak('Waiting...')
        time.sleep( 600 ) # 10 minutes
        eliza.so.printSpeak("Shall we continue our session?")
        break;

    #  Add the new question to the situationContext and submit
    situationContext.append({'role': 'user', 'content': f"{prompt}"})
    response = eliza.ai.submitMessages2(situationContext)
    #  Add the response to the context and print/speak it
    situationContext.append({'role': 'assistant', 'content': f"{response}"})
    eliza.so.printSpeak(response)


print('Done...')

