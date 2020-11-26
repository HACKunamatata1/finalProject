import pyxel

class Cell:
    __cx,__cy=0,0
    __image=""
    
    def __init__(self,x,y):
        self.__cx=x
        self.__cy=y
        self.__image="V"
    


class App:
    
    x=0
    sqX,sqY=0,0 #Coordenadas cursor para seleccionar celda
    WIDTH,HEIGHT=160,128
    grid=[]
    color=3
    fila=int(WIDTH/16)
    columna=int(HEIGHT/16)
    Max_Lemmings=5

    def __init__(self):
        pyxel.init(self.WIDTH,self.HEIGHT, caption="Lemmings")
       # pyxel.image(0).load(0, 0, "assets/pyxel_logo_38x16.png")
        pyxel.run(self.update, self.draw)
        pyxel.load("my_resource.pyxres")
        pyxel.image(0).load(0, 0, "assets/cat_16x16.png")
        pyxel.image(0).load(0, 16, "assets/cat_16x16.png")
        pyxel.image(0).load(0, 32, "assets/cat_16x16.png")
        pyxel.image(0).load(0, 48, "assets/cat_16x16.png")
        
        #create matrix        
        for i in range(self.fila):
            self.grid.append([])
            for j in range(self.columna):
                cell=Cell(i,j)
                cell.image="v"                 
                self.grid[i].append(cell)   
                                  
        pyxel.run(self.update, self.draw)


    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        pyxel.cls(0)
        pyxel.text(0, 0, "Level:", 1)
        pyxel.text(25, 0, "1", 1)
        pyxel.text(30, 0, "Alive:", 1)
        pyxel.text(59, 0, "Saved:", 1)
        pyxel.text(90, 0, "Died:", 1)
        pyxel.text(0, 15, "Ladders:", 1)
        pyxel.text(35, 15, "Umbrellas:", 1)
        pyxel.text(80, 15, "Blockers:", 1)
        #pyxel.blt(120, 15, 0, 0, 0, 38, 16)


App()
