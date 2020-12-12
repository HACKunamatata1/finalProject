from Constants import MAX_LADDERS,MAX_UMBRELLAS,MAX_BLOCKERS

class Score:

    """ THIS CLASS WILL DEFINE ALL THE SCORE PARAMETERS OF THE GAME"""

    def __init__(self):

        self.level = 1     # Note: there is only one level
        self.on_board = 0
        self.saved = 0
        self.died = 0
        self.ladders = MAX_LADDERS
        self.umbrellas = MAX_UMBRELLAS
        self.blockers = MAX_BLOCKERS
    
    # AND NOW WE WILL DEFINE ALL METHODS TO CHANGE THE SCORE WHILE THE GAME 
    # IS RUNNING
    
    def addlemming(self):
        self.on_board += 1

    def dellemming_died(self):
        self.on_board -= 1
        self.died += 1

    def dellemming_saved(self):
        self.on_board -= 1
        self.saved += 1
    
    def addLadder(self):
        self.ladders+=1
        
    def delLadder(self):
        self.ladders-=1

    def addUmbrella(self):
        self.umbrellas+=1

    def delUmbrella(self):
        self.umbrellas-=1

    def addBlocker(self):
        self.blockers+=1

    def delBlocker(self):
        self.blockers-=1

    