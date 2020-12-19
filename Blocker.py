class Blocker:

    """ BLOCKER TOOL TO MAKE LEMMINGS TRANSFORM AND MAKE OTHER LEMMINGS
    CHANGE DIRECTION. IT IS NOT A WALL, IT IS A TOOL TO TRANSFORM A LEMMING."""

    def __init__(self, bloc_x, bloc_y):

        #position atributes

        self.bloc_x = bloc_x
        self.bloc_y = bloc_y

        self.used = False
               
        # "USED" Attribute. This will allow us in all
        # tool classes to make a difference btwn used tools
        # and unused tools, so they can be removed without adding any tool to
        # the score board when they are used.
    
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
    
    @property
    def used(self):
        return self.__used
    
    @used.setter
    def used(self, used):
        self.__used = used

    