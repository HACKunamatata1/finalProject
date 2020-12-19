## IMPORTANT NOTE: THIS CLASS IS NOT IMPLEMENTED ON THE CODE. IT HAS TO BE
## ACTIVATED BY DISABLE COMMENTING THE CODE THAT GENERATES THE SUPERFLOOR
## AND ACTIVATING THE ONE THAT GENERATES LAVA. ALSO ACTIVATING THE LAVA INTERACTIONS
## ON THE UPDATE() FUNCTION OF MAINGAME.

## Comentario en español: en realidad la lava es el código original: en el pdf nos 
## pedis que generemos 7 suelos, pero era complicado programar con el suelo
## de abajo rodeado de lava, así que llenamos la parte de abajo con un gran suelo para
## evitar que los lemmings se muriesen al caer constantemente. Pero lo que pedís en el 
## pdf está implementado.

class Lava:

    """THIS WILL FILL THE BOTTOM OF THE BOARD WITH A SEA OF LAVA, EXCEPT THE
    GENERATED PLATFORM AT THE BOTTOM. IF A LEMMING TOUCHES LAVA IT WILL DIE.
    IT HAS THE SAME BEHAVIOUR AS A PLATFORM OBJECT, BUT WITH LAVA"""

    def __init__(self, lava_x, lava_y):

        #position attributes

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