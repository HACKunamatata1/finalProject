class Umbrella:

    """ UMBRELLA TOOL"""

    def __init__(self, umb_x, umb_y):

        self.umb_x = umb_x
        self.umb_y = umb_y
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