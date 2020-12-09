from Constants import *
from Score import *

class Lemming:


    def __init__(self,x,y):

        self.lemx = x
        self.lemy = y
        self.direction= "R" 
        self.falling= False
        self.falling_with_umbrella = False
        self.died = False
        self.sprite = "walking1_R"
        self.lava = False
        #"walking1_R","walking2_R", "walking1_L","walking2_L",
        # "falling", "died", ""Umbrella falling"", "SAVED"

    def changeDirection(self):
        if self.direction=="R":
            self.direction="L"
            self.lemx-=LEMMINGS_VELOCITY
            
        else:
            self.direction="R"
            self.lemx+=LEMMINGS_VELOCITY
            
    
    def move(self):
        if self.direction=="R" and self.falling == False:
            self.lemx+=LEMMINGS_VELOCITY
        elif self.direction=="L" and self.falling == False:
            self.lemx-=LEMMINGS_VELOCITY
        

    def fall(self):
        if self.falling == True and self.lava == False:
            self.lemy += LEMMINGS_VELOCITY
    
    def change_sprite(self, newsprite):
        
        self.sprite = newsprite
    
    def die(self):

        self.died = True
        self.sprite = "died"
        
        
         
        

    """
    @property
    def x(self):
        return self.__cx
    
    @x.setter
    def x(self,cx):
        self.__cx=cx

    @property
    def y(self):
        return self.__cy
    
    @y.setter
    def y(self,cy):
        self.__cy=cy

    @property
    def image(self):
        return self.__image
    
    @image.setter 
    def image(self,image):
        self.__image=image
    
    @property 
    def direction(self,direction):
        self.__direction
    
    @direction.setter
    def direction(self,direction):
        self.__direction=direction
    """
    

