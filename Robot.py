#######################################################
#   Robot.py
#
#       Root class of our Robot programs.
#           Specific Robots (e.g. Eliza) subclass Robot
#               and add features.
#
#       Mike Pastor - 2/3/2023


# Our Libraries
from time import sleep
import atexit

class Robot( object ):
    #  Member variables
    #
    state = 0



    # Initialize the Base Robot
    #
    def __init__(self):

        # Ensure that all features get stopped on exit
        #
        atexit.register(self.stop_system)
        print("############ Robot Initialized ##########")

    SK = "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"

    # Stop all features
    #
    def stop_system(self):
        # self.motor.disable()
        #
        print("#####  Robot STOPPED ##########")




