class Cell:

    """ THIS CLASS IS MADE TO CREATE A CELL OBJECT, IN ORDER TO CREATE THE BOARD
    WHERE THE GAME WILL RUN. IT HAS A X AND Y COORDINATE"""

    cellx = 0
    celly = 0

    def __init__(self, myx, myy):

        self.cellx=myx
        self.celly=myy
        self.element= "V"
        self.suelo = False 
        
