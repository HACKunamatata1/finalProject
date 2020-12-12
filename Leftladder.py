class Left_Ladder:

    """ LADDER TOOL """

    def __init__(self, ll_x, ll_y):

        self.ll_x = ll_x
        self.ll_y = ll_y
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