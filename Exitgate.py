class Exitgate:

    """CLASS FOR THE EXIT GATE. WHEN LEMMINGS HIT THE EXITGATE, THEY WILL
    DISSAPEAR FROM THE GAME AND ADD ONE SCORE UP ON THE "SAVED" SCOREBOARD """

    def __init__ (self, myx, myy):

        #position attributes

        self.exitgate_x = myx
        self.exitgate_y = myy

    @property
    def exitgate_x(self):
        return self.__exitgate_x
    
    @exitgate_x.setter
    def exitgate_x(self, myx):
        self.__exitgate_x = myx
    
    @property
    def exitgate_y(self):
        return self.__exitgate_y
    
    @exitgate_y.setter
    def exitgate_y(self, myy):
        self.__exitgate_y = myy