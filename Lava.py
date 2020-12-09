## IMPORTANT NOTE: THIS CLASS IS NOT IMPLEMENTED ON THE CODE. IT HAS TO BE
## ACTIVATED BY COMMENTING THE CODE THAT GENERATES THE SUPERFLOOR
## AND ACTIVATING THE ONE THAT GENERATES LAVA

class Lava:

    def __init__(self, lava_x, lava_y):

        self.lava_x = lava_x
        self.lava_y = lava_y
    
    @property

    def lava_x(self):
        return self.__lava_x

    @lava_x.setter

    def lava_x(self, lava_x):
        self.__lava_x = lava_x
    
    @property

    def lava_y(self):
        return self.__lava_y

    @lava_y.setter

    def lava_y(self, lava_y):
        self.__lava_y = lava_y