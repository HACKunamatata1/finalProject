class Cell:

    """ THIS CLASS IS TO CREATE A CELL OBJECT, IN ORDER TO CREATE THE BOARD
    WHERE THE GAME WILL RUN. IT HAS A X AND Y COORDINATE"""

    cellx = 0
    celly = 0
    image = ""

    def __init__(self, myx, myy):

        self.cellx=myx
        self.celly=myy
        self.image="E" 
        
