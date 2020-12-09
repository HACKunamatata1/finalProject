class Score:

#ALIVE, DIED....

    def __init__(self):

        self.level = 1
        self.alive = 0
        self.saved = 0
        self.died = 0
        self.ladders = 10
        self.umbrellas = 10
        self.blockers = 10
    
    def addlemming(self):
        self.alive += 1
    def dellemming(self):
        self.alive -= 1
    def addUmbrella(self):
        self.umbrellas+=1
    def delUmbrella(self):
        self.umbrellas-=1
    def addBlocker(self):
        self.blockers+=1
    def delBlocker(self):
        self.blockers-=1
    def addLadder(self):
        self.ladders+=1
    def delLadder(self):
        self.ladders-=1