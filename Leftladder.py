class Left_Ladder:

    """ LEFT LADDER TOOL. IT ALLOWS THE LEMMINGS TO CLIMB UP AND DOWN TROUGH
    PLATFORMS WITH A LADDER POINTING TO THE LEFT. """

    #IMPORTANT COMMENT: we didn't have to implement this tools correctly.
    # Lemmings are able to climb the ladders (not step by step, but teleporting
    # through 16 pixels) and reach lower platforms without dying, but they are
    # not able to reach higher platforms without dying and other problems.
    # (see bug report for further info)

    def __init__(self, ll_x, ll_y):

        #position attributes

        self.ll_x = ll_x
        self.ll_y = ll_y

        #"Used" attribute. Explained on Blocker Module.
        self.used = False

    @property
    def ll_x(self):
        return self.__ll_x
    
    @ll_x.setter
    def ll_x(self, ll_x):
        self.__ll_x = ll_x

    @property
    def ll_y(self):
        return self.__ll_y

    @ll_y.setter
    def ll_y(self, ll_y):
        self.__ll_y = ll_y
    
    @property
    def used(self):
        return self.__used
    
    @used.setter
    def used(self, used):
        self.__used = used