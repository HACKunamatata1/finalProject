from Constants import LEMMINGS_VELOCITY


class Lemming:

    """ THIS IS THE MAIN CLASS OF THE GAME. THIS CLASS DEFINES A
    LEMMING AND ALL ITS ATTRIBUTES: INTERACTIONS WITH OBJECTS, DIRECTION,
    STATE OF LIFE...ALSO, ALL THE METHODS USED IN THE GAME TO MAKE THE LEMMING
    ALSO INTERACT WITH ITS SURROUNDINGS."""


    def __init__(self,x,y):

        #position of the lemming (APPROACH IN PIXELS)

        self.lemx = x
        self.lemy = y

        #direction of the lemming (left or right)
        self.direction= "R"

        #state of falling (normal falling and umbrella falling)
     
        self.falling= False
        self.falling_with_umbrella = False     
        self.checker_umbrella = False          #just a checker of sound effect
        
        #state of life and appereance on the program/board: also deactivation

        self.died = False
        self.saved = False
        self.appeared = False
        self.checker_appeared = False  #just a checker of sound effect
        self.deactivate = False        #another checker for sound effect

        #collision with lava: if it is true the lemming won't move 
        #IMPORTANT: code not implemented/not useful (see info in lava module)
        self.lava = False

        #graphical sprite of the lemming

        self.sprite = ""

        ## USEFUL INFO: LIST OF SPRITES
        ## "walking_R", "walking_L","falling", "died",
        ## "Umbrella falling", "Blocker", "Builder"
        
        #state of the lemming when it touches a blocker tool

        self.being_blocker = False
        self.checker_blocker = False    #just a checker for sound effect

    # NOW IT COMES A LONG SPAGUETTI CODE WITH ALL THE PROPERTIES
    # (they dont do nothing but it is compulsory to put them)
    
    @property
    def lemx(self):
        return self.__lemx
    
    @lemx.setter
    def lemx(self, lemx):
        self.__lemx = lemx
    
    @property
    def lemy(self):
        return self.__lemy
    
    @lemy.setter
    def lemy(self, lemy):
        self.__lemy = lemy
         
    @property
    def direction(self):
        return self.__direction
    
    @direction.setter
    def direction(self, direction):
        self.__direction = direction

    @property
    def falling(self):
        return self.__falling
    
    @falling.setter
    def falling(self, falling):
        self.__falling = falling

    @property
    def falling_with_umbrella(self):
        return self.__falling_with_umbrella
    
    @falling_with_umbrella.setter
    def falling_with_umbrella(self, falling_with_umbrella):
        self.__falling_with_umbrella = falling_with_umbrella

    @property
    def checker_umbrella(self):
        return self.__checker_umbrella
    
    @checker_umbrella.setter
    def checker_umbrella(self, checker_umbrella):
        self.__checker_umbrella = checker_umbrella

    @property
    def died(self):
        return self.__died
    
    @died.setter
    def died(self, died):
        self.__died = died

    @property
    def saved(self):
        return self.__saved
    
    @saved.setter
    def saved(self, saved):
        self.__saved = saved

    @property
    def appeared(self):
        return self.__appeared
    
    @appeared.setter
    def appeared(self, appeared):
        self.__appeared = appeared

    @property
    def checker_appeared(self):
        return self.__checker_appeared
    
    @checker_appeared.setter
    def checker_appeared(self, checker_appeared):
        self.__checker_appeared = checker_appeared

    @property
    def deactivate(self):
        return self.__deactivate
    
    @deactivate.setter
    def deactivate(self, deactivate):
        self.__deactivate = deactivate   

    @property
    def sprite(self):
        return self.__sprite
    
    @sprite.setter
    def sprite(self, sprite):
        self.__sprite = sprite 
    
    @property
    def lava(self):
        return self.__lava
    
    @lava.setter
    def lava(self, lava):
        self.__lava = lava 

    @property
    def being_blocker(self):
        return self.__being_blocker
    
    @being_blocker.setter
    def being_blocker(self, being_blocker):
        self.__being_blocker = being_blocker  

    @property
    def checker_blocker(self):
        return self.__checker_blocker
    
    @checker_blocker.setter
    def checker_blocker(self, checker_blocker):
        self.__checker_blocker = checker_blocker   




    # NOW WE DEFINE ALL THE METHODS FOR THE LEMMING TO INTERACT WITH THE GAME 

    def move(self):

        """ MOVE THE LEMMING ALONG THE X axis"""

        if self.direction=="R" and self.falling == False:
            self.lemx+=LEMMINGS_VELOCITY
        elif self.direction=="L" and self.falling == False:
            self.lemx-=LEMMINGS_VELOCITY  
        
        
    def changeDirection(self):

        """ CHANGE THE DIRECTION OF THE LEMMING"""

        if self.direction=="R":
            self.direction="L"
            self.lemx-=LEMMINGS_VELOCITY
            
        else:
            self.direction="R"
            self.lemx+=LEMMINGS_VELOCITY
            
    def fall(self):

        """MOVE THE LEMMING ALONG THE Y AXIS"""

        if self.falling == True and self.lava == False:
            self.lemy += LEMMINGS_VELOCITY
    
    def change_sprite(self, newsprite):

        """METHOD TO CHANGE THE SPRITE OF THE LEMMING"""
        
        self.sprite = newsprite
    
    def die(self):

        """MAKE THE LEMMING DIE"""

        self.died = True
        self.sprite = "died"
    
    def save(self):

        """PUT THE LEMMING IN A SAVED STATE"""

        self.saved = True
    
    def dissapear(self):

        """MAKE THE LEMMING GRAPHICALLY DISSAPEAR FROM THE GAME"""

        self.appeared = False
        self.sprite = ""
        
    
    def umbrella_collision(self):

        """MAKE THE LEMMING COLLIDE WITH AN UMBRELLA"""

        self.falling_with_umbrella = True
        self.sprite = "Umbrella falling"
        self.checker_umbrella = True
        
        
    def converting_to_blocker(self): 

        """CONVERT THE LEMMING INTO A BLOCKER LEMMING WHEN IT TOUCHES A 
        BLOCKER TOOL"""

        self.being_blocker = True
        self.sprite = "Blocker"
        self.checker_blocker = True

    def collision_right_ladder_UP(self):
        """MAKE THE LEMMING CLIMB A RIGHT LADDER UP"""
        self.lemy-=16
        self.lemx+=16
    
    def collision_left_ladder_UP(self):
        """MAKE THE LEMMING CLIMB A LEFT LADDER UP"""
        self.lemy-=16
        self.lemx-=16

    # IMPORTANT COMMENT:
    # Names of these methods below are related to the direction of the lemming, not
    # with the orientation of the ladder, which is the opposite

    def collision_right_ladder_DOWN(self):
        """MAKE THE LEMMING CLIMB A LEFT LADDER DOWN"""
        self.lemy+=16
        self.lemx+=16
    
    def collision_left_ladder_DOWN(self):
        """MAKE THE LEMMING CLIMB A RIGHT LADDER DOWN"""
        self.lemy+=16
        self.lemx-=16

    # IMPORTANT COMMENT: we tried to implement the builder lemming, but it was
    # too dificult and we run out of time for it.
      
    # METHODS AND ATTRIBUTES NOT IMPLEMENTED: CONVERTING THE LEMMING INTO
    # A LADDER BUILDER LEMMING (we tried to implement this, but only sprites
    # on the pyxres are done, we need a correct implementation of the ladders to
    # make this step, but we didn't)
         
    """
    def converting_to_builder(self):

        #This is to change the sprite when encountering a ladder

            self.being_builder=True
            self.sprite="Builder"
            self.checker_ladder= True

    """