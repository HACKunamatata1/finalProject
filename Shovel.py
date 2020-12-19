class Shovel:

    """ THIS CLASS IS TO DEFINE THE SHOVEL EXTRA TOOL. WHEN TOUCHED, IT MAKES A
    "HOLE" ON THE PLATFORM BELOW THE LEMMING SO IT CAN IGNORE IT AND PASS THROUGH
    IT. (see Destroyed Platform module and bug report for further info)"""

    def __init__(self,x,y):

        #position attributes

        self.shovel_x = y
        self.shovel_y = y

        #"Used" attribute. Explained on Blocker Module.
        self.used = False