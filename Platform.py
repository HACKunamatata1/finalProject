
import random


class Platform:

    def __init__(self, platform_x, platform_y):

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
