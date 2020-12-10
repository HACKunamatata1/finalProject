class Blocker:

    def __init__(self, bloc_x, bloc_y):

        self.bloc_x = bloc_x
        self.bloc_y = bloc_y
        self.used = False
    
    @property
    def bloc_x(self):
        return self.__bloc_x
    
    @bloc_x.setter
    def bloc_x(self, bloc_x):
        self.__bloc_x = bloc_x

    @property
    def bloc_y(self):
        return self.__bloc_y

    @bloc_y.setter
    def bloc_y(self, bloc_y):
        self.__bloc_y = bloc_y

    