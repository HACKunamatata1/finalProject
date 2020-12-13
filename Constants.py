import random

"""
THIS FILE ONLY CONTAINS THE CONSTANTS THAT ARE GOING TO BE USED IN OUR PROGRAM.
THIS VARIABLES SHOULDN'T BE CHANGED, BUT THEY CAN BE CHANGED IN ORDER TO MODIFY
SOME ASPECTS OF THE PROGRAM

"""

WIDTH, HEIGHT = 256, 256    # GAME SIZE

BACKGROUND = 0              # BACKGROUND COLOR

TOTAL_PLATFORMS = 7         # NUMBER OF PLATFORMS. SHOULDN'T BE CHANGED IN THIS PROGRAM

LEMMINGS_VELOCITY = 0.4     # VELOCITY OF LEMMINGS. CAN BE CHANGED

MAX_LEMMINGS= random.randint(10,20)          # NUMBER OF LEMMINGS THAT WILL APPEAR. CAN BE CHANGED.

# Note: at the moment only one lemming appears, despite being more, and we dind't found
# out how to implement it

MAX_LADDERS = random.randint(5,10)
MAX_UMBRELLAS = random.randint(5,10)
MAX_BLOCKERS = random.randint(5,10)
<<<<<<< HEAD
MAX_SHOVELS = random.randint(5,10)
=======
>>>>>>> dccdd06491934ff053f0fd31534a848260499829
