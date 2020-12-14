#Importing Pyxel library and random library
import pyxel
import random

#Importing fixed variables from a Constants Module
from Constants import *
#Importing Cell class, Platform class and Score class
from Cell import *
from Score import *
from Platform import *
from Lava import *
#Importing entry and exit gates
from Entrygate import *
from Exitgate import *
#Importing Lemmings class
from Lemmings import *
#Importing tools
from Rightladder import *
from Leftladder import *
from Umbrella import *
from Blocker import *
from Shovel import *




        
class Maingame:
    
    """ HERE WE WILL DEFINE ALL THE GAME INITIAL VALUES FOR ALL PARAMETERS."""
    
    def __init__(self):
        
        self.backgroundcolor = BACKGROUND  # not very useful 
        pyxel.init(WIDTH, HEIGHT, caption = "Pyxel Lemmings")
        pyxel.load("assets/SPRITES.pyxres")
        

        pyxel.playm(0,loop=True)                     # PLAYING BACKGROUND MUSIC

        self.cursorX, self.cursorY = 0, 32           # INITIAL VALUES OF USER POINTER

        # GOD MODE: WHEN ACTIVATED, YOU CAN ADD PLATFORMS WHILE THE GAME IS RUNNING
        # AND YOU CAN STOP TIME OF LEMMINGS (stopping time variable is called ZAWARUDO)
        
        self.god_mode = False

        self.zawarudo = False

        # FIRST STEP: CREATING THE BOARD: we use the method of filling
        # a list with lists and creating a matrix

        self.cellrow=int(WIDTH/16)
        self.cellcolumn=int(HEIGHT/16)
        self.boardmatrix = []

        for i in range (self.cellrow):
            self.boardmatrix.append([])
            for j in range (self.cellcolumn):
                cell=Cell(i,j)                       ## using Cell from Cell module
                self.boardmatrix[i].append(cell)
        
        self.myscore = Score()                       ## using Score from Score module


        ## CREATING SUPERFLOOR: THIS IS FOR ENSURING LEMMINGS THAT FALL TO THE BOTTOM
        ## OF THE BOARD DONT CRASH THE GAME. IF YOU WANT THE LEMMINGS TO DIE WHEN 
        ## REACHING THE BOTTOM OF THE BOARD, YOU CAN ACTIVATE THE CODE 
        ## COMMENTED BELOW, CREATING LAVA CELLS AT THE BOTTOM OF THE BOARD:
        """
            for i in range(self.cellcolumn):
                cellcheck=self.boardmatrix[i][int(self.cellcolumn) - 1]
                cellcheck.cellclass= Lava(i, (int(self.cellcolumn) - 1))
        """

        for i in range(self.cellcolumn):
            cellcheck=self.boardmatrix[i][int(self.cellcolumn) - 1]
            cellcheck.cellclass= Platform(i, (int(self.cellcolumn) - 1))
        
        # SECOND STEP : CREATING THE PLATFORMS

        self.available_column_positions = (48,80,112,144,176,208,240) ## fixed values for starting platform x pos

        self.available_row_positions = (0,16,32,48,64)             ## fixed values for starting platform y pos

        self.platforms = []                                           ## list with all the platforms

        for i in range(0,TOTAL_PLATFORMS):

            ##FIRST WE CREATE A START PLATFORM OF 16X16 AND THEN WE EXTEND IT

            xposition = self.available_row_positions[random.randint(0,4)]
            yposition = self.available_column_positions[i]

            boardplatform_start = Platform(xposition, yposition)
            ###assigning the platform to the cell 
            self.boardmatrix[int(xposition/16)][int(yposition/16)].cellclass = Platform(xposition, yposition)
            
            self.platforms.append(boardplatform_start)

            length_of_floor = random.randint(4,9)  ###EXTENDING THE PLATFORMS

            for i in range(0,length_of_floor):
                xposition += 16
                boardplatform_prolong = Platform(xposition, yposition)
                self.boardmatrix[int(xposition/16)][int(yposition/16)].cellclass = Platform(xposition, yposition)                      
                self.platforms.append(boardplatform_prolong)

        # THIRD STEP: CREATE ENTRANCE AND EXIT GATES FOR THE LEMMINGS

        platcounter = len(self.platforms)

        ##ENTRY GATE
        
        self.entrygate_platform = self.platforms[random.randint(0, platcounter-1)]
        entrygate_final_xpos = self.entrygate_platform.platform_x
        entrygate_final_ypos = self.entrygate_platform.platform_y 
        self.entrygate = Entrygate(entrygate_final_xpos, entrygate_final_ypos - 16)
        ### assigning the gate to a cell
        self.boardmatrix[int(entrygate_final_xpos/16)][int((entrygate_final_ypos - 16)/16)].cellclass = Entrygate(entrygate_final_xpos, entrygate_final_ypos - 16)
        
        ##EXITGATE

        self.exitgate_platform = self.platforms[random.randint(0, platcounter-1)]

        ### HERE WE ENSURE THAT THE GATES DON'T OVERLAP THEMSELVES AND THAT THEY ARE IN DIFFERENT FLOORS

        while (self.exitgate_platform == self.entrygate_platform or 
                self.exitgate_platform.platform_y == self.entrygate_platform.platform_y):
            self.exitgate_platform = self.platforms[random.randint(0, platcounter)]

        exitgate_final_xpos = self.exitgate_platform.platform_x
        exitgate_final_ypos = self.exitgate_platform.platform_y 
        self.exitgate = Exitgate(exitgate_final_xpos, exitgate_final_ypos - 16)
        ### assigning the gate to a cell
        self.boardmatrix[int(exitgate_final_xpos/16)][int((exitgate_final_ypos - 16)/16)].cellclass = Exitgate(exitgate_final_xpos, exitgate_final_ypos - 16)


        # INITIALIZING THE LEMMINGS LISTS: 

        self.list_of_lemmings = []
        self.list_of_appeared_lemmings = []

        pyxel.run(self.update, self.draw)





    ########## UPDATE ############

    # WE WILL DEFINE VARIOUS UPDATE FUNCTIONS AND THEN PUTTING THEM
    # IN THE MAIN UPDATE() PYXEL FUNCTION  

    def update_player_arrows(self):
        
        """ THIS WILL DEFINE THE USER ACTIONS ON THE GAME THROUGH THE
        KEYBOARD, MOVING THE POINTER"""


        #QUITTING APP

        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        # MOVEMENTS OF THE RECTANGLE POINTER

        if pyxel.btnp(pyxel.KEY_RIGHT):
            if self.cursorX+16<=WIDTH-16:
                self.cursorX+=16
                pyxel.play(2,12)
        if pyxel.btnp(pyxel.KEY_LEFT):
            if self.cursorX-16>=0:
                self.cursorX-=16
                pyxel.play(2,12)
        if pyxel.btnp(pyxel.KEY_DOWN):
            if self.cursorY+16<=HEIGHT-16:
                self.cursorY+=16
                pyxel.play(2,12)
        if pyxel.btnp(pyxel.KEY_UP):
            if self.cursorY-16>=32:             ## HEADER LIMIT
                self.cursorY-=16
                pyxel.play(2,12)

        
        

    def update_tools_placement(self):

        """ THIS WILL DEFINE THE USER ACTIONS WITH THE LETTERS OF THE KEYBOARD:
        TOOLS PLACEMENT, TOOLS REMOVAL, AND GOD MODE ACTIONS"""

        ## IMPORTANT NOTE: FROM NOW ON WE USED ISINSTANCE() FUNCTION
        ## TO CHECK IF A GIVEN CELL CONTAINS SOME TYPE OF OBJECT (platforms, tools...)
        ## we didn't see this on the course but it is a very simple function and very useful
        ## for the program.


        # RIGHT LADDER

        if pyxel.btnp(pyxel.KEY_A):

            ## ALL THE COMMENTS OF THIS TOOL CAN BE APPLICABLE FOR ALL TOOLS.

            ##THESE ARE CHECKERS FOR THE PROGRAM TO ANALYZE THE POSITION OF THE
            ##USER POINTER.
            
            position_in_row = int(self.cursorY/16) 
            position_in_column = int(self.cursorX/16)
            cellsee = self.boardmatrix[position_in_column][position_in_row]

            ##First, we make the code for removing the tool

            if (isinstance(cellsee.cellclass, Right_Ladder) == True and
                cellsee.cellclass.used == False):
                cellsee.cellclass = None
                self.myscore.addLadder()
            else:
                ###placements of all tools
                if cellsee.cellclass == None:                           ### no tool in selected cell
                    if self.myscore.ladders != 0:
                        cellsee.cellclass = Right_Ladder(position_in_row, position_in_column)
                        self.myscore.delLadder()
                if isinstance(cellsee.cellclass, Umbrella) == True:     ### checking if umbrella is on cell
                    if self.myscore.ladders != 0:
                        if cellsee.cellclass.used == False:             ### checking if it is a placeholder or if it is used tool
                            self.myscore.addUmbrella()
                        cellsee.cellclass = Right_Ladder(position_in_row, position_in_column)
                        self.myscore.delLadder()
                        
                if (isinstance(cellsee.cellclass, Left_Ladder) == True  ### checking if left ladder is on cell
                    and cellsee.cellclass.used == False):
                    if self.myscore.ladders != 0:                       ### we dont make changes to score because right and left ladder are technically the same tool
                        cellsee.cellclass = Right_Ladder(position_in_row, position_in_column)
                        
                if isinstance(cellsee.cellclass, Blocker) == True:      ### checking if blocker is on cell
                    if self.myscore.ladders != 0:
                        if cellsee.cellclass.used == False:             ### checking if it is a placeholder or if it is used tool
                            self.myscore.addBlocker()
                        cellsee.cellclass = Right_Ladder(position_in_row, position_in_column)
                        self.myscore.delLadder()
            
            ### sound effect

            pyxel.play(3,9)            
            
        # LEFT LADDER        

        if pyxel.btnp(pyxel.KEY_S):

            position_in_row = int(self.cursorY/16) 
            position_in_column = int(self.cursorX/16)
            cellsee = self.boardmatrix[position_in_column][position_in_row]

            if (isinstance(cellsee.cellclass, Left_Ladder) == True and
                cellsee.cellclass.used == False):
                cellsee.cellclass = None
                self.myscore.addLadder()
            else:
                if cellsee.cellclass == None:
                    if self.myscore.ladders != 0:
                        cellsee.cellclass = Left_Ladder(position_in_row, position_in_column)
                        self.myscore.delLadder()

                if isinstance(cellsee.cellclass, Umbrella) == True:
                    if self.myscore.ladders != 0:
                        if cellsee.cellclass.used == False:
                            self.myscore.addUmbrella()
                        cellsee.cellclass = Left_Ladder(position_in_row, position_in_column)
                        self.myscore.delLadder()
                        
                if (isinstance(cellsee.cellclass, Right_Ladder) == True and
                    cellsee.cellclass.used == False):
                    if self.myscore.ladders != 0:
                        cellsee.cellclass = Left_Ladder(position_in_row, position_in_column)
                        
                if isinstance(cellsee.cellclass, Blocker) == True:
                    if self.myscore.ladders != 0:
                        if cellsee.cellclass.used == False:
                            self.myscore.addBlocker()
                        cellsee.cellclass = Left_Ladder(position_in_row, position_in_column)
                        self.myscore.delLadder()
            pyxel.play(3,9)            

        # UMBRELLA   

        if pyxel.btnp(pyxel.KEY_D):
            position_in_row = int(self.cursorY/16) 
            position_in_column = int(self.cursorX/16)
            cellsee = self.boardmatrix[position_in_column][position_in_row]

            if (isinstance(cellsee.cellclass, Umbrella) == True and
                cellsee.cellclass.used == False):
                    self.myscore.addUmbrella()
                    cellsee.cellclass = None
                
            else:
                if cellsee.cellclass == None:
                    if self.myscore.umbrellas != 0:
                        cellsee.cellclass = Umbrella(position_in_row, position_in_column)
                        self.myscore.delUmbrella()

                if isinstance(cellsee.cellclass, Left_Ladder) == True:
                    if self.myscore.umbrellas != 0:
                        if cellsee.cellclass.used == False:
                            self.myscore.addLadder()
                            cellsee.cellclass = Umbrella(position_in_row, position_in_column)
                            self.myscore.delUmbrella()
                        
                if isinstance(cellsee.cellclass, Right_Ladder) == True:
                    if self.myscore.umbrellas != 0:
                        if cellsee.cellclass.used == False:
                            self.myscore.addLadder()
                            cellsee.cellclass = Umbrella(position_in_row, position_in_column)
                            self.myscore.delUmbrella()
                        
                if isinstance(cellsee.cellclass, Blocker) == True:
                    if self.myscore.umbrellas != 0:
                        if cellsee.cellclass.used == False:
                            self.myscore.addBlocker()
                        cellsee.cellclass = Umbrella(position_in_row, position_in_column)
                        self.myscore.delUmbrella()
            pyxel.play(3,9)

        #BLOCKER                

        if pyxel.btnp(pyxel.KEY_F):
            position_in_row = int(self.cursorY/16) 
            position_in_column = int(self.cursorX/16)
            cellsee = self.boardmatrix[position_in_column][position_in_row]

            if (isinstance(cellsee.cellclass, Blocker) == True and
                cellsee.cellclass.used == False):
                    self.myscore.addBlocker()
                    cellsee.cellclass = None
                
            else:
                if cellsee.cellclass == None:
                    if self.myscore.blockers != 0:
                        cellsee.cellclass = Blocker(position_in_row, position_in_column)
                        self.myscore.delBlocker()

                if isinstance(cellsee.cellclass, Left_Ladder) == True:

                    if self.myscore.blockers != 0:
                        if cellsee.cellclass.used == False:
                            self.myscore.addLadder()
                            cellsee.cellclass = Blocker(position_in_row, position_in_column)
                            self.myscore.delBlocker()
                        
                if isinstance(cellsee.cellclass, Right_Ladder) == True:
                    if self.myscore.blockers != 0:
                        if cellsee.cellclass.used == False:
                            self.myscore.addLadder()
                            cellsee.cellclass = Blocker(position_in_row, position_in_column)
                            self.myscore.delBlocker()
                        
                if isinstance(cellsee.cellclass, Umbrella) == True:
                    if self.myscore.umbrellas != 0:
                        if cellsee.cellclass.used == False:
                            self.myscore.addUmbrella()
                        cellsee.cellclass = Blocker(position_in_row, position_in_column)
                        self.myscore.delBlocker()
            pyxel.play(3,9)
                        
        #just for testing(ignore this): 
        # CREATING USED OBJECTS FOR SCORE TESTING:
        # YOU CANNOT REMOVE USED LADDERS AND IF YOU REMOVE USED TOOLS THEY WONT 
        # BE ADDED TO TOOLS SCORE

        if pyxel.btnp(pyxel.KEY_G):
            position_in_row = int(self.cursorY/16) 
            position_in_column = int(self.cursorX/16)
            cellsee = self.boardmatrix[position_in_column][position_in_row] 
            cellsee.cellclass = Right_Ladder(position_in_row, position_in_column)
            cellsee.cellclass.used = True
        if pyxel.btnp(pyxel.KEY_H):
            position_in_row = int(self.cursorY/16) 
            position_in_column = int(self.cursorX/16)
            cellsee = self.boardmatrix[position_in_column][position_in_row]   
            cellsee.cellclass = Left_Ladder(position_in_row, position_in_column)
            cellsee.cellclass.used = True
        if pyxel.btnp(pyxel.KEY_J):
            position_in_row = int(self.cursorY/16) 
            position_in_column = int(self.cursorX/16)
            cellsee = self.boardmatrix[position_in_column][position_in_row]    
            cellsee.cellclass = Umbrella(position_in_row, position_in_column)
            cellsee.cellclass.used = True
        if pyxel.btnp(pyxel.KEY_K):
            position_in_row = int(self.cursorY/16) 
            position_in_column = int(self.cursorX/16)
            cellsee = self.boardmatrix[position_in_column][position_in_row]    
            cellsee.cellclass = Blocker(position_in_row, position_in_column)
            cellsee.cellclass.used = True



        
        #EXTRA FEATURES:
        #   SHOVEL: SHOVEL WILL BE USED ONE TIME (PLATFORM ARE DESTROYED ONCE) 
        #   SO THERE IS NO NEED TO MAKE A PLACE HOLDER FOR THIS ONE.
        #   SUBSTITUTION FOR OTHER TOOLS ARE NO IMPLEMENTED ON THIS ONE
        #   SPRITE OF DESTROYED PLATFORM IS DRAWN ON PYXEL EDITOR 
        #   UT WE DIN'T FIGURE OUT HOW TO DRAW IT ON THE GAME

        if pyxel.btnp(pyxel.KEY_E):

            position_in_row = int(self.cursorY/16) 
            position_in_column = int(self.cursorX/16)
            cellsee = self.boardmatrix[position_in_column][position_in_row]

            if (isinstance(cellsee.cellclass, Shovel) == True and
                cellsee.cellclass.used == False):
                    self.myscore.addShovel()
                    cellsee.cellclass = None
            else:
                if self.myscore.shovels != 0:
                    cellsee.cellclass = Shovel(position_in_row, position_in_column)
                    self.myscore.delShovel() 

            pyxel.play(3,9)   
                            
                            
            
            
        

        #   GOD MODE: WE CAN CREATE AS MUCH PLATFORMS AS WE WANT WITH THIS CODE BELOW.
        #   ALSO, THE ZAWARUDO VARIABLE ALLOWS THE PLAYER TO STOP TIME, AND THEREFORE,
        #   THE LEMMINGS MOVEMENT.

        ## ACTIVATE GOD MODE
        if pyxel.btnp(pyxel.KEY_V): 
            self.god_mode = True
            pyxel.play(3,15)
        ## DISABLE GOD MODE
        if pyxel.btnp(pyxel.KEY_B): 
            self.god_mode = False
            pyxel.play(3,15)

        
        if self.god_mode == True:
            
            ##CREATING PLATFORMS
            if pyxel.btnp(pyxel.KEY_P):
                position_in_row = int(self.cursorY/16) 
                position_in_column = int(self.cursorX/16)
                cellsee = self.boardmatrix[position_in_column][position_in_row]
                cellsee.cellclass = Platform(position_in_row, position_in_column)  
                
            ## STOPPING TIME (ZAWARUDO MODE)
            if pyxel.btnp(pyxel.KEY_Z):
                self.zawarudo = True
                pyxel.play(3,16)
            ## DISABLING ZAWARUDO MODE
            if pyxel.btnp(pyxel.KEY_X):
                self.zawarudo = False
                pyxel.play(3,16)


    
    def update_initializing_lemmings(self):

        """ THIS WILL CREATE ALL THE LEMMINGS AND MAKE THEM APPEAR IN ORDER"""
        # Note: Despite we create a large ammount of lemmings, they dont appear 
        # one by one and we don't know why and how to do it.

        for i in range(MAX_LEMMINGS):
            if len(self.list_of_lemmings)<MAX_LEMMINGS:
                self.list_of_lemmings.append(Lemming(self.entrygate.entrygate_x, self.entrygate.entrygate_y))
                self.myscore.addlemming()
            
        counter = 0
        counter = pyxel.frame_count 

        if counter % 50 == 0:
            if len(self.list_of_appeared_lemmings)< len(self.list_of_lemmings):
                self.list_of_appeared_lemmings.append(Lemming(self.entrygate.entrygate_x, self.entrygate.entrygate_y)) 
                #pyxel.play(2,10) sound of lemmings appearing
                for i in self.list_of_appeared_lemmings:
                        i.appeared = True
                        i.checker_appeared = True
        
                     
                


    # THIS IS ALL THE CODE TO LEMMING MOVEMENT AND INTERACTION BETWEEN OBJECTS
    
    def update_lemmings_movement_and_tools(self):
        
        

        for i in self.list_of_appeared_lemmings:

            ##cellclass CHECKERS: RIGHT, LEFT AND BELOW
            self.cellclass_of_cell_right = self.boardmatrix[int(i.lemx//16)+1][int(i.lemy//16)].cellclass
            self.cellclass_of_cell_below_right = self.boardmatrix[int(i.lemx//16)][int((i.lemy//16)+1)].cellclass
            self.cellclass_of_cell_left = self.boardmatrix[int(i.lemx//16)][int(i.lemy//16)].cellclass
            self.cellclass_of_cell_below_left = self.boardmatrix[int(i.lemx//16)][int(i.lemy//16)+1].cellclass
            
            self.cellclass_of_cell_right_blocker = self.boardmatrix[int(i.lemx//16)+1][int(i.lemy//16)].cellclass
            self.cellclass_of_cell_left_blocker = self.boardmatrix[int(i.lemx//16)-1][int(i.lemy//16)].cellclass
            # MOVEMENT AND INTERACTION WITH ALL OBJECTS
            
            if self.zawarudo == False:

                if i.appeared == True:                             ## check if lemmings have appeared

                    if i.checker_appeared == True:                 ## just to establish the initial sprite
                        i.change_sprite("walking_R")
                        i.checker_appeared = False

                    if i.died == False or i.saved == False:        ## check that they aren't saved or they didn't die
                        
                        ## COLLISION WITH SIDE PLATFORMS AND BLOCKER LEMMINGS

                        if ((isinstance(self.cellclass_of_cell_right, Platform) == True 
                            or isinstance(self.cellclass_of_cell_left, Platform) == True)
                            or(isinstance(self.cellclass_of_cell_right_blocker, Blocker_lemming) == True 
                                or isinstance(self.cellclass_of_cell_left_blocker, Blocker_lemming) == True)):
                            
                            if i.direction == "R":
                                i.change_sprite("walking_L")
                                i.changeDirection()                 ### changing directions of lemming
                            else:
                                i.change_sprite("walking_R")
                                i.changeDirection()

                        #COLLISION WITH SHOVEL AND DESTROYING THE PLATFORM BELOW:

                        elif isinstance(self.cellclass_of_cell_right, Shovel) == True:
                            self.cellclass_of_cell_below_right = Destroyed_platform(int(i.lemx//16),int(i.lemx//16)+1)
                            self.cellclass_of_cell_right.used = True          
                        elif isinstance(self.cellclass_of_cell_left, Shovel) == True:
                            self.cellclass_of_cell_below_right = Destroyed_platform(int(i.lemx//16),int(i.lemx//16)+1)
                            self.cellclass_of_cell_left.used = True
                        
                        # IF NOTHING OF ABOVE HAPPENS, LET THE LEMMING MOVE:   
                        else:
                            if i.being_blocker == False:            ### checking that they don't move if they are a blocker
                                i.move()
                            
                    ## COLLISION WITH BLOCKER OBJECT TO TRANSFORM THE LEMMING
                    
                    if isinstance(self.cellclass_of_cell_right, Blocker) == True:
                        if i.checker_blocker == False:              ### just a checker to play the sound effect correctly
                            pyxel.play(2,13)
                        i.converting_to_blocker()                   ### transforming the lemming
                        self.cellclass_of_cell_right.used = True    ### making the blocker tool dissapear
                        
                        self.boardmatrix[int(i.lemx/16)][int(i.lemy/16)].cellclass = Blocker_lemming(i.lemx,i.lemy) ### creating a Lemming blocker on the stablished position

                    if isinstance(self.cellclass_of_cell_left, Blocker) == True:

                        if i.checker_blocker == False:
                            pyxel.play(2,13)
                        i.converting_to_blocker()
                        self.cellclass_of_cell_left.used = True
                        
                        self.boardmatrix[int(i.lemx/16)][int(i.lemy/16)].cellclass = Blocker_lemming(i.lemx,i.lemy) ### creating a Lemming blocker on the stablished position


                    ## COLLISION WITH EXIT GATE: SAVING THE LEMMINGS AND ENDING THE GAME
                    
                    if  (isinstance(self.cellclass_of_cell_right, Exitgate) == True 
                            or isinstance(self.cellclass_of_cell_left, Exitgate) == True):

                            i.save()                               ###saving lemming
                            i.dissapear()                          ###making it dissapear
                            if i.deactivate == False:              ###checker for sound effect
                                i.deactivate = True
                                pyxel.play(3,11)
                                self.myscore.dellemming_saved()    ###adding to score  
                    
                    ## COLLISION WITH SHOVEL
                    


                ## IMPORTANT NOTE: THERE IS A SOMETIMES BUG WHEN FALLING FROM THE LEFT OF A PLATFORM. 
                ## DESPITE BEING SEARCHING SOLUTIONS FOR HOURS
                ## WE COULDN'T FIND ONE USEFUL, WE ARE SORRY.

                ## FALLING LEMMING

                    if i.died == False or i.saved == False:
                    
                        if (isinstance(self.cellclass_of_cell_below_right, Platform) == False 
                            or (isinstance(self.cellclass_of_cell_below_left, Platform) == False and i.direction == "L")):
                            
                            i.falling = True
                            i.fall()
                            i.change_sprite("falling")
                            if i.falling_with_umbrella == True:         
                                i.change_sprite("Umbrella falling")
                        
                ## COLLISION WITH UMBRELLA OBJECT

                    if isinstance(self.cellclass_of_cell_below_right, Umbrella) == True:
                        pyxel.play(2,8)                                    ### sound effect
                        i.umbrella_collision()                              
                        self.cellclass_of_cell_below_right.used = True     ### making umbrella an used tool
                        
                            
                
                ## REACHING FLOOR WITH AN UMBRELLA
                
                    if (i.falling == True and isinstance(self.cellclass_of_cell_below_right, Platform) == True):
                        if i.falling_with_umbrella == True:
                            #disabling falling attributes
                            i.falling = False
                            i.falling_with_umbrella = False

                            ### making the lemming move again
                            i.move()
                            if i.direction == "R":
                                i.change_sprite("walking_R")
                            else:
                                i.change_sprite("walking_L")

                        else:               
                            ## THIS WILL HAPPEN IF LEMMING FALL WITHOUT UMBRELLA. IT WILL DIE
                            ## AND DISSAPEAR
                            i.die() 
                            if i.deactivate == False:
                                i.deactivate = True
                                pyxel.play(3,14)
                                self.myscore.desllemming_died()
                            
                ##ENCOUNTER WITH RIGHT LADDER

                    if(isinstance(self.cellclass_of_cell_left,Right_Ladder) or isinstance(self.cellclass_of_cell_right,Right_Ladder)):
                        i.direction="U"
                        i.move()
                        i.falling = False
                        i.fall()
                        if((isinstance(self.cellclass_of_cell_below_left,Platform)==False 
                        or isinstance(self.cellclass_of_cell_below_right,Platform)==False) and
                        isinstance(self.cellclass_of_cell_below_left,Right_Ladder)==True):
                            i.direction="U"
                            i.move()
                            i.falling = False
                            i.fall()
                            i.sprite="Builder"

                        elif(isinstance(self.cellclass_of_cell_below_right,None)
                        or isinstance(self.cellclass_of_cell_below_left,None)):
                            i.falling=True
                            i.fall()
                        else:
                            i.falling=True
                            i.fall()
                        
                ##ENCOUNTER WITH LEFT LADDER

                    if(isinstance(self.cellclass_of_cell_left,Left_Ladder) or isinstance(self.cellclass_of_cell_right,Left_Ladder)):
                        i.direction="D"
                        i.move()
                        i.falling = False
                        i.fall()
                        if((isinstance(self.cellclass_of_cell_below_left,Platform)==False 
                        or isinstance(self.cellclass_of_cell_below_right,Platform)==False) and
                        isinstance(self.cellclass_of_cell_below_left,Left_Ladder)==True):
                            i.direction="D"
                            i.move()
                            i.falling = False
                            i.fall()
                            i.sprite="Builder"

                        elif(isinstance(self.cellclass_of_cell_below_right,None)
                        or isinstance(self.cellclass_of_cell_below_left,None)):
                            i.falling=True
                            i.fall()
                        else:
                            i.falling=True
                            i.fall()
                        
                    # LEMMINGS DIE WHEN REACHING LAVA (CODE NOT IMPLEMENTED, READ INFO IN LAVA MODULE)       
                    """
                    if (self.lemming.falling == True and isinstance(self.cellclass_of_cell_below_right, Lava) == True):
                            self.lemming.lava = True
                            self.lemming.died = True
                    """
                    # COLLISION WITH EDGES OF THE GAME
                    
                    if i.lemx >= WIDTH -16 or i.lemx <= 0:
                        i.changeDirection()
                        if i.direction == "R":
                            i.change_sprite("walking_R")
                        else:
                            i.change_sprite("walking_L")

    # CALLING THE MAIN UPDATE FUNCTION

    def update(self):
        self.update_initializing_lemmings()
        self.update_player_arrows()
        self.update_lemmings_movement_and_tools()
        self.update_tools_placement()
        
        
    ########### DRAW ############
    
        
      
    def draw(self):

        """ THIS FUNCTION IS DEFINED TO DRAW ALL THE GAME ELEMENTS"""

        #pyxel.cls(self.backgroundcolor)
        
        pyxel.blt(0,32,1,0,0,256,224)                    # BACKGROUND WALLPAPER IF YOU DONT WANT CLS
        pyxel.blt(0,0,2,0,0,256,32)                      # SCORE BACKGROUND
         
        # DRAWING ALL THE HEADER TEXT WITH THE SCORE BOARD 
        #(USED STRING FORMATTING TO AVOID ATTRIBUTE ERRORS(ENCODE UTF-8))

        pyxel.text(8,8, "Level:", pyxel.frame_count%16)
        pyxel.text(36,8, ("%d" %(self.myscore.level)), 10) 
        pyxel.text(80,8, "Alive:", pyxel.frame_count%16)
        pyxel.text(108,8, ("%d" %(self.myscore.on_board)), 10)
        pyxel.text(150,8, "Saved:", pyxel.frame_count%16)
        pyxel.text(180,8,("%d" %(self.myscore.saved)), 10)
        pyxel.text(210,8, "Died:", pyxel.frame_count%16)
        pyxel.text(235,8,("%d" %(self.myscore.died)), 10)
        pyxel.text(0,22, "Ladders:", 2)
        pyxel.text(34,22,("%d" %(self.myscore.ladders)), 10)
        pyxel.text(57,22, "Umbrellas:", 6)
        pyxel.text(96,22, ("%d" %(self.myscore.umbrellas)), 10)
        pyxel.text(124,22, "Blockers:", 11)
        pyxel.text(162,22,("%d" %(self.myscore.blockers)), 10)
        pyxel.text(198,22, "Shovels:", 0)
        pyxel.text(230,22,("%d" %(self.myscore.shovels)), 10)

        pyxel.line(0,31,255,31,10)          # LINE TO SEPARATE THE HEADER WITH THE BOARD

       
        #DRAWING ENTRY AND EXIT GATE:

        pyxel.blt(self.entrygate.entrygate_x, self.entrygate.entrygate_y,0,0,32,16,16,0)
        pyxel.blt(self.exitgate.exitgate_x,self.exitgate.exitgate_y, 0,16,32,16,16,0)

        # DRAWING SPRITES OF LEMMINGS WHEN THEY COLLIDE WITH THINGS,
        # AND WHEN THEY MOVE, FALL AND DIE.

        for i in self.list_of_appeared_lemmings:
        
            if i.deactivate == False:
                if i.sprite == "walking_R":
                    if pyxel.frame_count % 5 == 0:
                        pyxel.blt(i.lemx, i.lemy,0,32,16,16,16,0)
                    else:
                        pyxel.blt(i.lemx, i.lemy,0,32,64,16,16,0)
                    
                if i.sprite == "walking_L":
                    if pyxel.frame_count % 5 == 0:
                        pyxel.blt(i.lemx, i.lemy,0,48,48,16,16,0)
                    else:
                        pyxel.blt(i.lemx, i.lemy,0,48,64,16,16,0)   
                if i.sprite == "Umbrella falling":
                    pyxel.blt(i.lemx, i.lemy,0,32,48,16,16,0)
                if i.sprite == "falling":
                    pyxel.blt(i.lemx, i.lemy,0,0,64,16,16,0)
                if i.sprite == "Blocker":
                    pyxel.blt(i.lemx, i.lemy,0,16,64,16,16,0)
                if i.sprite =="Builder":                            #Draws the sprite for the ladder builder
                    pyxel.blt(i.lemx,i.lemy,0,0,80,16,16,0)
            if i.sprite == "died":
                pyxel.blt(i.lemx, i.lemy,0,32,32,16,16,0)
                
        
        # DRAWING ALL THE CELL cellclass OF THE BOARD DEPENDING ON THE .cellclass ATTRIBUTE
        # We check all the cells and we draw what's inside of it.

        for i in range(self.cellrow):            
            for j in range(self.cellcolumn):
                cellcheck=self.boardmatrix[i][j]
                if isinstance(cellcheck.cellclass, Right_Ladder) == True:
                    if cellcheck.cellclass.used == False:
                        pyxel.blt(cellcheck.cellx*16, cellcheck.celly*16, 0, 32,0,16,16,0)
                    else:
                        pyxel.blt(cellcheck.cellx*16, cellcheck.celly*16, 0, 0,0,16,16,0)
                
                if isinstance(cellcheck.cellclass, Left_Ladder) == True:
                    if cellcheck.cellclass.used == False:
                        pyxel.blt(cellcheck.cellx*16, cellcheck.celly*16, 0, 16,48,16,16,0)
                    else:
                        pyxel.blt(cellcheck.cellx*16, cellcheck.celly*16, 0, 0,48,16,16,0)
                
                if isinstance(cellcheck.cellclass, Umbrella) == True:
                    if cellcheck.cellclass.used == False:
                        pyxel.blt(cellcheck.cellx*16, cellcheck.celly*16, 0, 48,0,16,16,0)
                    else:
                        pyxel.blt(cellcheck.cellx*16, cellcheck.celly*16, 0, 16,0,16,16,0)
                
                if isinstance(cellcheck.cellclass, Blocker) == True:
                    if cellcheck.cellclass.used == False:
                        pyxel.blt(cellcheck.cellx*16, cellcheck.celly*16, 0, 16,16,16,16,0)
                    else:
                        pyxel.blt(cellcheck.cellx*16, cellcheck.celly*16, 0, 0,16,16,16,0)
                
                if isinstance(cellcheck.cellclass, Shovel) == True:
                    if cellcheck.cellclass.used == False:
                        pyxel.blt(cellcheck.cellx*16, cellcheck.celly*16, 0,0,96,16,16,0)
                    else:
                        pyxel.blt(cellcheck.cellx*16, cellcheck.celly*16, 0,0,80,16,16,0)

                if isinstance(cellcheck.cellclass, Platform) == True:
                    pyxel.blt(cellcheck.cellx*16, cellcheck.celly*16, 0, 48,16,16,16,0)
                
                if isinstance(cellcheck.cellclass, Destroyed_platform) == True:
                    pyxel.blt(cellcheck.cellx*16, cellcheck.celly*16, 0, 16,80,16,16,0)

                # LAVA NOT IMPLEMENTED
                if isinstance(cellcheck.cellclass, Lava) == True:
                    pyxel.blt(cellcheck.cellx*16, cellcheck.celly*16, 0, 48,32,16,16,0)
                
        # DRAWING PLAYER POINTER        
                
        pyxel.rectb(self.cursorX, self.cursorY, 16, 16, 8)  

        # DRAWING WINNING AND LOSING FACES (Happy and sad)

        if self.myscore.died == MAX_LEMMINGS:
            pyxel.blt(96,96,2,0,32,64,64)
        if self.myscore.saved == MAX_LEMMINGS:
            pyxel.blt(96,96,2,64,32,64,64)

#And finally....STARTING OUR APP

Maingame()