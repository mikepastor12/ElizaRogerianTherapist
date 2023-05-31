###############################################################
#    OpenAIObject.py
#
#      Provide a Robot interface to the Open AI - ChatGPT model
#
#           https://platform.openai.com/account/api-keys
#
#      Mike Pastor 2/3/2023

import openai


class OpenAIObject():

    #
    # #  openai.api_key = "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"
    # openai.api_key = "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"
    #
    # openai.api_key = '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'
    openai.api_key = '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'
    model_engine = "text-davinci-003"
    # prompt = "Hello, how are you today?"


    # Initialize the Open AI object
    #
    def __init__(self):

        print("############ OPENAI Initialized ##########")


    def do_completion( self, sentence ):

        completion = openai.Completion.create(
            engine = self.model_engine,
            prompt = sentence,
            max_tokens = 1024,
            n = 1,
            stop = None,
            temperature = 0.5 )

        response = completion.choices[0].text

        return response

#
# ai = OpenAIObject()
# response = ai.do_completion( 'hello brave new world')
# print( response )
# ai = OpenAIObject()
# response = ai.do_completion( 'hello brave new world')
# print( response )

