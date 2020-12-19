class Blocker_lemming:

    """ BLOCKER LEMMING CLASS. IT WILL APPEAR IN THE GAME WHEN
    A LEMMING COLLIDES WITH A BLOCKER TOOL."""

    def __init__(self,x,y):

        #position attributes
        
        self.x = x
        self.y = y
    
    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self, x):
        self.__x = x
    
    @property
    def y(self):
        return self.__y
    
    @y.setter
    def y(self, y):
        self.__y = y