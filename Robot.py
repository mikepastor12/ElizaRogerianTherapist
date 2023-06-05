########################################################################
#   Robot.py
#
#       Eliza Rogerian Therapist – ChatGPT Version
#
#       Root class of all our Robot programs.
#           Specific Robots (e.g. Eliza, PennwickRover) subclass Robot
#               and add features.
#
#       Mike Pastor - 6/5/2023

import atexit


#   A Robot is an entity
#       All Robots should shutdown cleanly on exit.
#
class Robot( object ):
    #  Member variables
    #
    state = 0

    # Initialize the Base Robot
    #
    def __init__(self):

        # Ensure that all features get stopped on exit
        #
        atexit.register(self.StopSystem)
        print("############ Base Robot Initialized ##########")


    # Stop all features
    #
    def StopSystem(self):
        # self.motor.disable()
        #
        print("#####  Robot STOPPED ##########")

###################################################################



