#####################################################
#       Eliza.py
#
#       Build the next generation of the famous Eliza program
#           using ChatGPT and modern voice capabilities
#
#       Eliza was one of the first AI programs introduced in the 1960s.
#       I implemented a version of Eliza using C language in early 1990s
#           and build on some of those ideas here...
#
#       Michael Pastor - June 5, 2023

from Robot import Robot

from SoundObject import SoundObject  # Our voice commands
from OpenAIObject import OpenAIObject  # Our Open AI  commands

import pandas as pd
import numpy as np
import random


class Eliza( Robot ):

    ai = OpenAIObject()

    so = SoundObject()

    print("############ Eliza Initialized ##########")

    def get_response(  self  ):

        return

