import pyxel

class gridSquare:
    #properties coordX and coordY,initialize 0,0
    #global variables or @property
    __cx=0
    __cy=0
    def __init__(self,x,y):
        self.cx=x
        self.cy=y


class App:
     board=[]
    #Call creation process in an object
    #Init process to declare variables,to set initial values
    #images 16*16 pyxels
    MYSIZE=16
    HEIGHT=128
    WIDTH=160
    def __init__(self):
        pyxel.init(160, 120, caption="Hello Pyxel")
        pyxel.image(0).load(0, 0, "img/sprites.png")
        for i in range (self.WIDTH/self.MYSIZE):
            self.board.append([])
            for j in range (self.HEIGHT/self.MYSIZE):
                obj=Cell(5,17)
                self.board[i].append([])


        cell in my grid
        
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        pyxel.cls(0)
        pyxel.text(55, 41, "Hello, Pyxel!", pyxel.frame_count % 16)
        pyxel.blt(0,0, 0, 0, 0, 15, 15)


App()
