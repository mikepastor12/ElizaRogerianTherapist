#######################################################
#    ElizaMain.py
#
#    Main loop for our robot.

#       Mike Pastor 2/3/2023


from Eliza import Eliza
import SoundHeader as sh   # Our voice commands


# Our robot is instantiated here
#
eliza = Eliza()

print('Eliza Rogerian Therapist is running!')

sh.speak('Hello I am Eliza the Rogerian Therapist ')

while True:
    # message = input("? ")
    # parse as list
    # query = sh.parseCommand().lower().split()
    query = sh.parseCommand().lower()

    ints = eliza.predict_class( query )

    res, tag = eliza.get_response(  ints, eliza.elizaIntents )
    sh.speak( res )

    if tag == 'goodbye':
        exit(0)

print('Done...')

