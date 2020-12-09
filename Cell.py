class Cell:

    """ THIS CLASS IS MADE TO CREATE A CELL OBJECT, IN ORDER TO CREATE THE BOARD
    WHERE THE GAME WILL RUN. IT HAS A X AND Y COORDINATE"""

    

    def __init__(self, x, y):

    # APPROACH IN POSITIONS OF A MATRIX

        self.cellx=x
        self.celly=y
        
        self.cellclass = None
        self.used = False
        
        self.entrygate = False
        self.lemming = False
        

"""
    @property
        return self.__cellx
    @cellx.setter
        self.__cellx = cellx
    @property
        return self.__cellx
    @celly.setter
        self.__cellx = cellx
    @property
        return self.__cellx
    @element.setter
        self.__cellx = cellx        
"""