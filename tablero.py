import pyxel
from constants import *
from cell import *
import random


class Maingame:

    WIDTH, HEIGHT = 256,256
    cursorX, cursorY = 16,16
    cellroW=int(WIDTH/16)
    cellcolumn=int(HEIGHT/16)
    boardmatrix = []
    color = 0
    lines=[]
    def __init__(self):

        pyxel.init(self.WIDTH, self.HEIGHT, caption = "Pyxel Lemmings")

        for i in range (self.cellroW):
            self.boardmatrix.append([])
            for j in range (self.cellcolumn):
                cell=Cell(i,j)  # HERE WE CALL THE OBJECT
                cell.image = "v"
                self.boardmatrix[i].append(cell)
    
      
        for i in range(3):
            placed=True
            while placed:
                randomNum=random.randint(32,255)
                if not randomNum in self.lines:
                    self.lines.append(randomNum) 
                    placed=False

        pyxel.run(self.update, self.draW)



    def update(self):
        
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        #Movimientos rectangulo
        if pyxel.btnp(pyxel.KEY_RIGHT):
            if self.cursorX+16<=self.WIDTH-16:
                self.cursorX+=16
        if pyxel.btnp(pyxel.KEY_LEFT):
            if self.cursorX-16>=0:
                self.cursorX-=16
        if pyxel.btnp(pyxel.KEY_DOWN):
            if self.cursorY+16<=self.HEIGHT-16:
                self.cursorY+=16
        if pyxel.btnp(pyxel.KEY_UP):
            if self.cursorY-16>=32:
                self.cursorY-=16
        if pyxel.btnp(pyxel.KEY_SPACE):
            position_in_roW = int(self.cursorY/16)
            position_in_column = int(self.cursorX/16)
            self.boardmatrix[position_in_roW][position_in_column].image = "s"

    def draW(self):
        pyxel.cls(self.color)
        pyxel.rectb(self.cursorX, self.cursorY, 16, 16, 1)
        pyxel.line(0,32,255,32,10)
        lines=[]
        for i in self.lines:
            pyxel.line(0,i,64,i,7)
            


        for i in range(self.cellroW):            
            for j in range(self.cellcolumn):
                cellcheck=self.boardmatrix[i][j]
                #pyxel.text(cell.x*16, cell.y*16, cell.image,1)
                if cell.image=="s":
                    pyxel.blt(cell.x*16, cell.y*16, 0, 0, 0,16,16,5)                    
                else:
                    pyxel.text(cell.x*16, cell.y*16, cell.image,5)
                    

Maingame()
        





