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




        
class Maingame:


    def __init__(self):
        
        self.backgroundcolor = BACKGROUND  
        pyxel.init(WIDTH, HEIGHT, caption = "Pyxel Lemmings")
        pyxel.load("assets/SPRITES.pyxres")

        pyxel.playm(0,loop=True)                     # PLAYING BACKGROUND MUSIC

        self.cursorX, self.cursorY = 0, 32           # INITIAL VALUES OF USER POINTER

        # FIRST STEP: CREATING THE BOARD

        self.cellrow=int(WIDTH/16)
        self.cellcolumn=int(HEIGHT/16)
        self.boardmatrix = []

        for i in range (self.cellrow):
            self.boardmatrix.append([])
            for j in range (self.cellcolumn):
                cell=Cell(i,j)                       # using Cell from Cell module
                self.boardmatrix[i].append(cell)
        
        self.myscore = Score()                       # using Score from Score module

        ## CREATING SUPERFLOOR: THIS IS FOR ENSURING LEMMINGS THAT FALL TO THE BOTTOM
        # OF THE BOARD DONT CRASH THE GAME. IF YOU WANT THE LEMMINGS TO DIE WHEN 
        ## REACHING THE BOTTOM OF THE BOARD, YOU CAN ACTIVATE THE CODE 
        # COMMENTED BELOW, CREATING LAVA CELLS AT THE BOTTOM OF THE BOARD:
        """
            for i in range(self.cellcolumn):
                cellcheck=self.boardmatrix[i][int(self.cellcolumn) - 1]
                cellcheck.cellclass= Lava(i, (int(self.cellcolumn) - 1))
        """

        for i in range(self.cellcolumn):
            cellcheck=self.boardmatrix[i][int(self.cellcolumn) - 1]
            cellcheck.cellclass= Platform(i, (int(self.cellcolumn) - 1))
        
        ## SECOND STEP : CREATING THE PLATFORMS

        self.available_column_positions = (48,80,112,144,176,208,240)

        self.available_row_positions = (0,16,32,48,64,80)

        self.platforms = []

        for i in range(0,TOTAL_PLATFORMS):

            #FIRST WE CREATE A START PLATFORM OF 16X16 AND THEN WE EXTEND IT

            xposition = self.available_row_positions[random.randint(0,4)]
            yposition = self.available_column_positions[i]

            boardplatform_start = Platform(xposition, yposition)
            self.boardmatrix[int(xposition/16)][int(yposition/16)].cellclass = Platform(xposition, yposition)
            self.platforms.append(boardplatform_start)

            length_of_floor = random.randint(4,9)  #EXTENDING THE PLATFORMS

            for i in range(0,length_of_floor):
                xposition += 16
                boardplatform_prolong = Platform(xposition, yposition)
                self.boardmatrix[int(xposition/16)][int(yposition/16)].cellclass = Platform(xposition, yposition)                      
                self.platforms.append(boardplatform_prolong)

        ## THIRD STEP: CREATE ENTRANCE AND EXIT GATES FOR THE LEMMINGS

        platcounter = len(self.platforms)

        ###ENTRY GATE
        
        self.entrygate_platform = self.platforms[random.randint(0, platcounter-1)]
        entrygate_final_xpos = self.entrygate_platform.platform_x
        entrygate_final_ypos = self.entrygate_platform.platform_y 
        self.entrygate = Entrygate(entrygate_final_xpos, entrygate_final_ypos - 16)
        
        ###EXITGATE

        self.exitgate_platform = self.platforms[random.randint(0, platcounter-1)]

        # HERE WE ENSURE THAT THE GATES DON'T OVERLAP THEMSELVES AND THAT THEY ARE IN DIFFERENT FLOORS

        while (self.exitgate_platform == self.entrygate_platform or 
                self.exitgate_platform.platform_y == self.entrygate_platform.platform_y):
            self.exitgate_platform = self.platforms[random.randint(0, platcounter)]

        exitgate_final_xpos = self.exitgate_platform.platform_x
        exitgate_final_ypos = self.exitgate_platform.platform_y 
        self.exitgate = Exitgate(exitgate_final_xpos, exitgate_final_ypos - 16)

        # INITIALIZING THE LEMMINGS: AT THE MOMENT THERE IS ONLY ONE LEMMING

        self.list_of_lemmings = []
        #for i in range(0, MAX_LEMMINGS):
        self.lemming = Lemming(self.entrygate.entrygate_x, self.entrygate.entrygate_y)
        self.list_of_lemmings.append(self.lemming)

        self.myscore.addlemming()
        
        
        pyxel.run(self.update, self.draw)

    #### UPDATE #####   

    def update_player_arrows(self):

        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        # MOVEMENTS OF THE RECTANGLE POINTER

        if pyxel.btnp(pyxel.KEY_RIGHT):
            if self.cursorX+16<=WIDTH-16:
                self.cursorX+=16
        if pyxel.btnp(pyxel.KEY_LEFT):
            if self.cursorX-16>=0:
                self.cursorX-=16
        if pyxel.btnp(pyxel.KEY_DOWN):
            if self.cursorY+16<=HEIGHT-16:
                self.cursorY+=16
        if pyxel.btnp(pyxel.KEY_UP):
            if self.cursorY-16>=32:             # HEADER LIMIT
                self.cursorY-=16

        
        # THIS IS ALL THE CODE DESIGNED FOR THE TOOLS PLACEMENT 
        
        ## IMPORTANT NOTE: FROM NOW ON WE USED ISINSTANCE() FUNCTION
        ## TO CHECK IF A GIVEN CELL CONTAINS SOME TYPE OF OBJECT (platforms, tools...)
        ## we didn't see this on the course but it is a very simple function and very useful
        ## for the program.

    def update_tools_placeement(self):

        # RIGHT LADDER

        if pyxel.btnp(pyxel.KEY_A):
            
            position_in_row = int(self.cursorY/16) 
            position_in_column = int(self.cursorX/16)
            cellsee = self.boardmatrix[position_in_column][position_in_row]

            if (isinstance(cellsee.cellclass, Right_Ladder) == True and
                cellsee.cellclass.used == False):

                cellsee.cellclass = None
                self.myscore.addLadder()
            else:
                if cellsee.cellclass == None:
                    if self.myscore.ladders != 0:
                        cellsee.cellclass = Right_Ladder(position_in_row, position_in_column)
                        self.myscore.delLadder()
                if isinstance(cellsee.cellclass, Umbrella) == True:
                    if self.myscore.ladders != 0:
                        if cellsee.cellclass.used == False:
                            self.myscore.addUmbrella()
                        cellsee.cellclass = Right_Ladder(position_in_row, position_in_column)
                        self.myscore.delLadder()
                        
                if (isinstance(cellsee.cellclass, Left_Ladder) == True 
                    and cellsee.cellclass.used == False):
                    if self.myscore.ladders != 0:
                        cellsee.cellclass = Right_Ladder(position_in_row, position_in_column)
                        
                if isinstance(cellsee.cellclass, Blocker) == True:
                    if self.myscore.ladders != 0:
                        if cellsee.cellclass.used == False:
                            self.myscore.addBlocker()
                        cellsee.cellclass = Right_Ladder(position_in_row, position_in_column)
                        self.myscore.delLadder()
                        
            
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
                        
        #just for testing(ignore this): CREATING USED OBJECTS FOR SCORE TESTING
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
        

        ## GOD MODE: WE CAN CREATE AS MUCH PLATFORMS AS WE WANT WITH THIS CODE BELOW

        if pyxel.btnp(pyxel.KEY_P):
            position_in_row = int(self.cursorY/16) 
            position_in_column = int(self.cursorX/16)
            cellsee.cellclass = Platform(position_in_row, position_in_column)



    
    # THIS IS ALL THE CODE TO LEMMING MOVEMENT AND INTERACTION BETWEEN OBJECTS
    
    def update_lemmings_movement(self):
        
        ##cellclass CHECKERS

        self.cellclass_of_cell_right = self.boardmatrix[int(self.lemming.lemx//16)+1][int(self.lemming.lemy//16)].cellclass
        self.cellclass_of_cell_below_right = self.boardmatrix[int(self.lemming.lemx//16)][int((self.lemming.lemy//16)+1)].cellclass
        self.cellclass_of_cell_left = self.boardmatrix[int(self.lemming.lemx//16)][int(self.lemming.lemy//16)].cellclass
        self.cellclass_of_cell_below_left = self.boardmatrix[int(self.lemming.lemx//16)][int(self.lemming.lemy//16)+1].cellclass

        ## COLLISION WITH SIDE FLOORS AND BLOCKERS

        if  ((isinstance(self.cellclass_of_cell_right, Platform) == True or isinstance(self.cellclass_of_cell_left, Platform) == True) or
            (isinstance(self.cellclass_of_cell_right, Blocker) == True or isinstance(self.cellclass_of_cell_left, Blocker) == True)):
            
            if self.lemming.direction == "R":
                self.lemming.change_sprite("walking1_L")
                self.lemming.changeDirection()
            else:
                self.lemming.change_sprite("walking1_R")
                self.lemming.changeDirection()
        else:
            self.lemming.move()
        
     

        ## THERE IS A BUG WHEN FALLING FROM THE LEFT OF A PLATFORM. DESPITE BEING SEARCHING SOLUTIONS FOR HOURS
        ## WE COULDN'T FIND ONE USEFUL, WE ARE SORRY.

        ## FALLING LEMMING
        
        if (isinstance(self.cellclass_of_cell_below_right, Platform) == False 
            or (isinstance(self.cellclass_of_cell_below_left, Platform) == False and self.lemming.direction == "L")):
            
            self.lemming.falling = True
            self.lemming.fall()
            self.lemming.change_sprite("falling")
            if self.lemming.falling_with_umbrella == True:
                self.lemming.change_sprite("Umbrella falling")

        
        ## COLLISION WITH UMBRELLA OBJECT

        if isinstance(self.cellclass_of_cell_below_right, Umbrella) == True:
            self.cellclass_of_cell_below_right.used = True 
            self.lemming.change_sprite("Umbrella falling")
            self.lemming.falling_with_umbrella = True
        
        ## REACHING FLOOR WITH AN UMBRELLA
        
        if (self.lemming.falling == True and isinstance(self.cellclass_of_cell_below_right, Platform) == True):
            if self.lemming.falling_with_umbrella == True:
                self.lemming.falling = False
                self.lemming.falling_with_umbrella = False
                self.lemming.move()
                if self.lemming.direction == "R":
                    self.lemming.change_sprite("walking1_R")
                else:
                    self.lemming.change_sprite("walking1_L")

                
            else:
                self.lemming.die()
                
        # LEMMINGS DIE WHEN REACHING LAVA (CODE NOT IMPLEMENTED, READ INFO IN LAVA MODULE)       
        """
        if (self.lemming.falling == True and isinstance(self.cellclass_of_cell_below_right, Lava) == True):
                self.lemming.lava = True
                self.lemming.died = True
        """
        # COLLISION WITH EDGES OF THE GAME
            
        if self.lemming.lemx >= WIDTH -16 or self.lemming.lemx <= 0:
            self.lemming.changeDirection()
            if self.lemming.direction == "R":
                self.lemming.change_sprite("walking1_L")
            else:
                self.lemming.change_sprite("walking1_R")


    #def update_lemming_using_tools(self): ????

        

    def update(self):
        self.update_player_arrows()
        self.update_lemmings_movement()
        self.update_tools_placeement()


    #### DRAW ######
    
        
      
    def draw(self):

        pyxel.cls(self.backgroundcolor)
        
        #pyxel.blt(0,32,2,0,0,256,224)                    # BACKGROUND WALLPAPER IF YOU DONT WANT CLS


        # DRAWING ALL THE HEADER TEXT WITH THE SCORE BOARD 
        #(USED STRING FORMATTING TO AVOID ATTRIBUTE ERRORS(ENCODE UTF-8))

        pyxel.text(0,8, "Level:", pyxel.frame_count%16)
        pyxel.text(24,8, ("%d" %(self.myscore.level)), 10) 
        pyxel.text(56,8, "Alive:", pyxel.frame_count%16)
        pyxel.text(80,8, ("%d" %(self.myscore.alive)), 10)
        pyxel.text(112,8, "Saved:", pyxel.frame_count%16)
        pyxel.text(136,8,("%d" %(self.myscore.saved)), 10)
        pyxel.text(168,8, "Died:", pyxel.frame_count%16)
        pyxel.text(188,8,("%d" %(self.myscore.died)), 10)
        pyxel.text(0,24, "Ladders:", 4)
        pyxel.text(32,24,("%d" %(self.myscore.ladders)), 10)
        pyxel.text(64,24, "Umbrellas:", 6)
        pyxel.text(104,24, ("%d" %(self.myscore.umbrellas)), 10)
        pyxel.text(144,24, "Blockers:", 8)
        pyxel.text(180,24,("%d" %(self.myscore.blockers)), 10)

        pyxel.line(0,31,255,31,10)          # LINE TO SEPARATE THE HEADER WITH THE BOARD

       
        #DRAWING ENTRY AND EXIT GATE:

        pyxel.blt(self.entrygate.entrygate_x, self.entrygate.entrygate_y,0,0,32,16,16)
        pyxel.blt(self.exitgate.exitgate_x,self.exitgate.exitgate_y, 0,16,32,16,16)

        # DRAWING SPRITES OF LEMMINGS WHEN THEY COLLIDE WITH THINGS

        if self.lemming.sprite == "walking1_R":
            pyxel.blt(self.lemming.lemx, self.lemming.lemy,0,32,16,16,16)
        if self.lemming.sprite == "walking1_L":
            pyxel.blt(self.lemming.lemx, self.lemming.lemy,0,48,48,16,16)
        if self.lemming.sprite == "Umbrella falling":
            pyxel.blt(self.lemming.lemx, self.lemming.lemy,0,32,48,16,16)
        if self.lemming.sprite == "falling":
            pyxel.blt(self.lemming.lemx, self.lemming.lemy,0,0,64,16,16)
        if self.lemming.sprite == "died":
            pyxel.blt(self.lemming.lemx, self.lemming.lemy,0,32,32,16,16)
        
        # DRAWING ALL THE CELL cellclassS OF THE BOARD DEPENDING ON THE .cellclass ATTRIBUTE
       
        for i in range(self.cellrow):            
            for j in range(self.cellcolumn):
                cellcheck=self.boardmatrix[i][j]
                if isinstance(cellcheck.cellclass, Right_Ladder) == True:
                    if cellcheck.cellclass.used == False:
                        pyxel.blt(cellcheck.cellx*16, cellcheck.celly*16, 0, 32,0,16,16)
                    else:
                        pyxel.blt(cellcheck.cellx*16, cellcheck.celly*16, 0, 0,0,16,16)
                
                if isinstance(cellcheck.cellclass, Left_Ladder) == True:
                    if cellcheck.cellclass.used == False:
                        pyxel.blt(cellcheck.cellx*16, cellcheck.celly*16, 0, 16,48,16,16)
                    else:
                        pyxel.blt(cellcheck.cellx*16, cellcheck.celly*16, 0, 0,48,16,16)
                
                if isinstance(cellcheck.cellclass, Umbrella) == True:
                    if cellcheck.cellclass.used == False:
                        pyxel.blt(cellcheck.cellx*16, cellcheck.celly*16, 0, 48,0,16,16)
                    else:
                        pyxel.blt(cellcheck.cellx*16, cellcheck.celly*16, 0, 16,0,16,16)
                
                if isinstance(cellcheck.cellclass, Blocker) == True:
                    if cellcheck.cellclass.used == False:
                        pyxel.blt(cellcheck.cellx*16, cellcheck.celly*16, 0, 16,16,16,16)
                    else:
                        pyxel.blt(cellcheck.cellx*16, cellcheck.celly*16, 0, 0,16,16,16)
                
                if isinstance(cellcheck.cellclass, Platform) == True:
                    pyxel.blt(cellcheck.cellx*16, cellcheck.celly*16, 0, 48,16,16,16)

                if isinstance(cellcheck.cellclass, Lava) == True:
                    pyxel.blt(cellcheck.cellx*16, cellcheck.celly*16, 0, 48,32,16,16)
                
                #if cellcheck.cellclass == "LAVA":
                    #pyxel.blt(cellcheck.cellx*16, cellcheck.celly*16 + 8, 0, 48, 40, 16,8)
                    
        pyxel.rectb(self.cursorX, self.cursorY, 16, 16, 9)  # DRAWING THE PLAYER POINTER


#STARTING OUR APP

Maingame()