import pyxel
import random

from Constants import *
from Cell import *
from Score import *
from Entrygate import *
from Exitgate import *


        
class Maingame:

    wid, hei = WIDTH, HEIGHT                        # values from Constants module

    backgroundcolor = BACKGROUND                    # INITIALIZE BACKGROUND COLOR


    def __init__(self):

        pyxel.init(self.wid, self.hei, caption = "Pyxel Lemmings")

        self.cursorX, self.cursorY = 0, 33      # initial values of user pointer

        # CREATING THE BOARD
        self.cellrow=int(self.wid/16)
        self.cellcolumn=int(self.hei/16)
        self.boardmatrix = []

        for i in range (self.cellrow):
            self.boardmatrix.append([])
            for j in range (self.cellcolumn):
                cell=Cell(i,j)                      # using Cell from Cell module
                self.boardmatrix[i].append(cell)
        
        self.myscore = Score()                      # using Score from Score module


        
        pyxel.run(self.update, self.draw)

    #### UPDATE #####   

    def update_player_arrows(self):

        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        # MOVEMENTS OF THE RECTANGLE POINTER

        if pyxel.btnp(pyxel.KEY_RIGHT):
            if self.cursorX+16<=self.wid-16:
                self.cursorX+=16
        if pyxel.btnp(pyxel.KEY_LEFT):
            if self.cursorX-16>=0:
                self.cursorX-=16
        if pyxel.btnp(pyxel.KEY_DOWN):
            if self.cursorY+16<=self.hei-16:
                self.cursorY+=16
        if pyxel.btnp(pyxel.KEY_UP):
            if self.cursorY-16>=32:             # HEADER LIMIT
                self.cursorY-=16
        if pyxel.btnp(pyxel.KEY_W):
            position_in_row = int(self.cursorY/16) 
            position_in_column = int(self.cursorX/16)
            self.boardmatrix[position_in_column][position_in_row].element = "L"
        if pyxel.btnp(pyxel.KEY_E):
            position_in_row = int(self.cursorY/16) 
            position_in_column = int(self.cursorX/16)
            self.boardmatrix[position_in_column][position_in_row].element = "U"
        if pyxel.btnp(pyxel.KEY_R):
            position_in_row = int(self.cursorY/16) 
            position_in_column = int(self.cursorX/16)
            self.boardmatrix[position_in_column][position_in_row].element = "B"
        

    def update(self):
        self.update_player_arrows()

    #### DRAW ######
    
        
      
    def draw(self):

        pyxel.cls(self.backgroundcolor)                     # BACKGROUND COLOR

        pyxel.rectb(self.cursorX, self.cursorY, 16, 16, 1)  # DRAWING THE PLAYER POINTER

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

        pyxel.line(0,32,255,32,10)          # LINE TO SEPARATE THE HEADER WITH THE BOARD

        """
        for i in range(self.cellrow):            
            for j in range(self.cellcolumn):
                cellcheck=self.boardmatrix[i][j]
                if cellcheck.image == "P":
                    pyxel.text(cellcheck.cellx*16, cellcheck.celly*16, cellcheck.image,6)
                else:
                    pyxel.text(cellcheck.cellx*16, cellcheck.celly*16, cellcheck.image,6)
        """

        for i in range(self.cellrow):            
            for j in range(self.cellcolumn):
                cellcheck=self.boardmatrix[i][j]
                #pyxel.text(cell.x*16, cell.y*16, cell.image,1)
                if cellcheck.element=="L":
                    pyxel.text(cellcheck.cellx*16, cellcheck.celly*16, cellcheck.element,5)
                if cellcheck.element=="U":
                    pyxel.text(cellcheck.cellx*16, cellcheck.celly*16, cellcheck.element,5)                    
                if cellcheck.element=="B":

                    pyxel.blt(cellcheck.cellx*16, cellcheck.celly*16, 1, 0,0,16,16)
                    """
                    pyxel.text(cellcheck.cellx*16, cellcheck.celly*16, cellcheck.element,5)             
                    """
                  

Maingame()