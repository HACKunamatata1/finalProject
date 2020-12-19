class Right_Ladder:

    """ RIGHT LADDER TOOL. IT ALLOWS THE LEMMINGS TO CLIMB UP AND DOWN TROUGH
    PLATFORMS WITH A LADDER POINTING TO THE RIGHT. """

    #IMPORTANT COMMENT: we didn't have to implement this tools correctly.
    # Lemmings are able to climb the ladders (not step by step, but teleporting
    # through 16 pixels) and reach lower platforms without dying, but they are
    # not able to reach higher platforms without dying and other problems...
    # (see bug report for further info)


    def __init__(self, rl_x, rl_y):

        #position attributes

        self.rl_x = rl_x
        self.rl_y = rl_y

        #"Used" attribute. Explained on Blocker Module.
        self.used = False

    @property
    def rl_x(self):
        return self.__rl_x
    
    @rl_x.setter
    def rl_x(self, rl_x):
        self.__rl_x = rl_x

    @property
    def rl_y(self):
        return self.__rl_y

    @rl_y.setter
    def rl_y(self, rl_y):
        self.__rl_y = rl_y