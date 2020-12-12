from Constants import LEMMINGS_VELOCITY


class Lemming:

    """ THIS IS THE MAIN CLASS OF THE GAME. THIS CLASS DEFINES A
    LEMMING AND ALL ITS ATTRIBUTES. INTERACTIONS WITH OBJECTS, DIRECTION,
    STATE OF LIFE..."""


    def __init__(self,x,y):

        #position
        self.lemx = x
        self.lemy = y

        #direction
        self.direction= "R"

        #state of falling
     
        self.falling= False
        self.falling_with_umbrella = False
        self.checker_umbrella = False #just a checker of sound effect
        
        #state of life and appereance on the program: also deactivation
        self.died = False
        self.saved = False
        self.appeared = False
        self.checker_appeared = False  #just a checker of sound effect
        self.deactivate = False

        #collision with lava: if it is true the lemming won't move
        self.lava = False

        #sprite of the lemming
        self.sprite = ""

        ## LIST OF SPRITES:
        ## "walking1_R","walking2_R", "walking1_L","walking2_L",
        ## "falling", "died", ""Umbrella falling"", 
        
        #state of blocker tool touching
        self.being_blocker = False
        self.checker_blocker = False
         
         
     # NOW WE DEFINE ALL THE METHODS FOR THE LEMMING TO INTERACT WITH THE GAME 

    def move(self):
        if self.direction=="R" and self.falling == False:
            self.lemx+=LEMMINGS_VELOCITY
        elif self.direction=="L" and self.falling == False:
            self.lemx-=LEMMINGS_VELOCITY  
        
    def changeDirection(self):

        if self.direction=="R":
            self.direction="L"
            self.lemx-=LEMMINGS_VELOCITY
            
        else:
            self.direction="R"
            self.lemx+=LEMMINGS_VELOCITY
            
    def fall(self):

        if self.falling == True and self.lava == False:
            self.lemy += LEMMINGS_VELOCITY
    
    def change_sprite(self, newsprite):
        
        self.sprite = newsprite
    
    def die(self):

        self.died = True
        self.sprite = "died"
    
    def save(self):

        self.saved = True
    
    def dissapear(self):

        self.appeared = False
        self.sprite = ""
        
    
    def umbrella_collision(self):

        self.falling_with_umbrella = True
        self.sprite = "Umbrella falling"
        self.checker_umbrella = True
        
        
    def converting_to_blocker(self): 

        self.being_blocker = True
        self.sprite = "Blocker"
        self.checker_blocker = True
         
        

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



    
class Blocker_lemming:

    """ BLOCKER LEMMING CLASS. IT WILL APPEAR IN THE GAME WHEN
    A LEMMING COLLIDES WITH A BLOCKER TOOL"""

    def __init__(self,x,y):

        self.x = x
        self.y = y
