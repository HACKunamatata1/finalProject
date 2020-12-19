
class Platform:

    """THIS WIL DEFINE A PLATFORM. ATTENTION: A PLATFORM IS NOT A FLOOR.
    PLATFORMS ONLY OCUPPY ONE CELL. FLOORS ARE GENERATED ON THE MAINGAME() CLASS"""

    def __init__(self, platform_x, platform_y):

        #position attributes

        self.platform_x = platform_x
        self.platform_y = platform_y
    
    @property

    def platform_x(self):
        return self.__platform_x

    @platform_x.setter

    def platform_x(self, platform_x):
        self.__platform_x = platform_x
    
    @property

    def platform_y(self):
        return self.__platform_y

    @platform_y.setter

    def platform_y(self, platform_y):
        self.__platform_y = platform_y


