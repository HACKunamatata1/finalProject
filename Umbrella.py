class Umbrella:

    """ UMBRELLA TOOL. IT MAKES THE LEMMING FALL WITHOUT RISK OF DYING
    WHEN REACHING A PLATFORM BELOW IT"""

    def __init__(self, umb_x, umb_y):

        #position attributes

        self.umb_x = umb_x
        self.umb_y = umb_y

        #"Used" attribute. Explained on Blocker Module.
        self.used = False

    @property
    def umb_x(self):
        return self.__umb_x
    
    @umb_x.setter
    def umb_x(self, umb_x):
        self.__umb_x = umb_x

    @property
    def umb_y(self):
        return self.__umb_y

    @umb_y.setter
    def umb_y(self, umb_y):
        self.__umb_y = umb_y