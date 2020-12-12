class Blocker:

    """ BLOCKER TOOL TO MAKE LEMMINGS TRANSFORM AND MAKE OTHER LEMMINGS
    CHANGE DIRECTION"""
    
    # Note: since, at the moment only one lemming is technically implemented, the only way to make
    # it change direction is activating god mode and placing platforms on the sides
    # of the lemming 

    def __init__(self, bloc_x, bloc_y):

        self.bloc_x = bloc_x
        self.bloc_y = bloc_y
        self.used = False       # "USED" Attribute
    
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

    