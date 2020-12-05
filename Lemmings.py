class Lemmings:
    __cx,__cy=0,0
    __image=[]
    __direction="L"
    __images=[]


    def __init__(self,x,y,direction,icons,fall):
        self.cx=x
        self.cy=y
        self.direction=direction 
        self.images=icons
        self.image=icons[0:2]
        self.falling=fall

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
    
    def changeDirection(self):
        if self.__direction=="R":
            self.__direction="L"
            self.__cx-=1
            self.image=[self.__images[0],self.__images[1]]
        else:
            self.__direction="R"
            self.__cx+=1   
            self.image=[self.__images[0],self.__images[1]]
    
    def move(self):
        if self.direction=="R":
            self.__cx+=1
        elif self.direction=="L":
            self.__cx-=1
        else:
            self.__cy+=1
    

