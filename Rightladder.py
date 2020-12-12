class Right_Ladder:

    """ RIGHT LADDER TOOL """
    
    def __init__(self, rl_x, rl_y):

        self.rl_x = rl_x
        self.rl_y = rl_y
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