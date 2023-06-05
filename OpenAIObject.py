###############################################################
#    OpenAIObject.py
#
#      Provide a Robot interface to the Open AI - ChatGPT model
#
#       You Need a valid OpenAI key here -  See this site
#           https://platform.openai.com/account/api-keys
#
#      Mike Pastor 6/5/2023

import openai
import json

class OpenAIObject():

    ###########################################################################
    #   You Need a valid OpenAI key here -
    #      https://platform.openai.com/account/api-keys
    #
    # openai.api_key = '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'


    #  Which LLM to use
    model_engine = "gpt-3.5-turbo"

    # Initialize the Open AI object
    #
    def __init__(self):

        print("############ Eliza OpenAIObject Initialized ##########")

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

    def doCompletion( self, sentence ):

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
# response = ai.submitMessages( 'hello brave new world')
# print( response )
# ai = OpenAIObject()
# response = ai.do_completion( 'hello brave new world')
# print( response )

