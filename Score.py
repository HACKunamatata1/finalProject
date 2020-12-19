from Constants import MAX_LADDERS,MAX_UMBRELLAS,MAX_BLOCKERS, MAX_SHOVELS

class Score:

    """ THIS CLASS WILL DEFINE ALL THE SCORE PARAMETERS OF THE GAME, SHOWN ABOVE """

    def __init__(self):

        # Note: there is only one level. Not multiple levels were implemented
        self.level = 1     
        
        self.on_board = 0                   # lemmings on board
        self.saved = 0                      # lemmings that were saved
        self.died = 0                       # lemmings that died

        # Number of tools available

        self.ladders = MAX_LADDERS          
        self.umbrellas = MAX_UMBRELLAS
        self.blockers = MAX_BLOCKERS
        self.shovels = MAX_SHOVELS
    
    # AND NOW WE WILL DEFINE ALL METHODS TO UPDATE THE SCORE WHILE THE GAME 
    # IS RUNNING
    
    def addlemming(self):
        """ADD LEMMING WHEN ONE APPEARS"""
        self.on_board += 1

    def dellemming_died(self):
        """TRIGGERED WHEN A LEMMING DIES"""
        self.on_board -= 1
        self.died += 1

    def dellemming_saved(self):
        """TRIGGERED WHEN A LEMMING IS SAVED"""
        self.on_board -= 1
        self.saved += 1
    
    def addLadder(self):
        """TRIGGERED WHEN A LADDER IS DELETED FROM THE BOARD"""
        self.ladders+=1
        
    def delLadder(self):
        """TRIGGERED WHEN A LADDER IS ADDED ON THE BOARD """
        self.ladders-=1

    def addUmbrella(self):
        """TRIGGERED WHEN A UMBRELLA IS DELETED FROM THE BOARD """
        self.umbrellas+=1

    def delUmbrella(self):
        """TRIGGERED WHEN A UMBRELLA IS ADDED ON THE BOARD """
        self.umbrellas-=1

    def addBlocker(self):
        """TRIGGERED WHEN A BLOCKER TOOL IS DELETED FROM THE BOARD """
        self.blockers+=1

    def delBlocker(self):
        """TRIGGERED WHEN A BLOCKER TOOL IS ADDED ON THE BOARD"""
        self.blockers-=1
    
    def addShovel(self):
        """TRIGGERED WHEN A SHOVEL IS DELETED FROM THE BOARD """
        self.shovels+=1

    def delShovel(self):
        """TRIGGERED WHEN A SHOVEL IS ADDED ON THE BOARD """
        self.shovels-=1

    