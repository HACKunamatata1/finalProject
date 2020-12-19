
class Entrygate:

    """ CLASS FOR THE ENTRY GATE: THE ELEMENT OF THE GAME THAT WILL MAKE THE
    THE LEMMINGS SPAWN IN THE BOARD"""

    def __init__(self, myx,myy):

        #position attributes

        self.entrygate_x = myx
        self.entrygate_y = myy

    @property
    def entrygate_x(self):
        return self.__entrygate_x
    
    @entrygate_x.setter
    def entrygate_x(self, myx):
        self.__entrygate_x = myx
    
    @property
    def entrygate_y(self):
        return self.__entrygate_y
    
    @entrygate_y.setter
    def entrygate_y(self, myy):
        self.__entrygate_y = myy

    