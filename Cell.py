class Cell:

    """ THIS CLASS IS MADE TO CREATE A CELL OBJECT, IN ORDER TO CREATE THE BOARD
    WHERE THE GAME WILL RUN. IT HAS A X AND Y COORDINATE AND IT IS NOT VISIBLE
    IN THE GAME, ITS JUST A POSITIONAL REPRESENTATION OF ALL THE THINGS CONTAINED 
    ON THE BOARD"""
    

    def __init__(self, x, y):

    # IMPORTANT COMMENT: THIS IS APPROACHED IN POSITIONS OF A MATRIX, NOT IN PIXELS

        #position attributes

        self.cellx=x
        self.celly=y
        
        # VERY IMPORTANT ATTRIBUTE. This will allow us to "see" whats inside a cell
        # on the board, so we can interact with other parts of the program related
        # to lemming collisions, tools placements...
        
        self.cellclass = None 

    @property
    def cellx(self):
        return self.__cellx

    @cellx.setter
    def cellx(self, cellx):
        self.__cellx = cellx

    @property
    def celly(self):
        return self.__celly

    @celly.setter
    def celly(self, celly):
        self.__celly = celly
    
    @property
    def cellclass(self):
        return self.__cellclass

    @cellclass.setter
    def cellclass(self, cellclass):
        self.__cellclass = cellclass

    