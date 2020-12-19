class Destroyed_platform:

    """ THIS DEFINES A DESTROYED PLATFORM. WHEN A SHOVEL IS TOUCHED,
    THE PLATFORM BELOW DISSAPEARS (the sprite of the original 
    platform doesn't dissapear but the platform is deleted, see bugs 
    report for further info)AND LEMMINGS ARE ABLE TO GO DOWN THROUGH 
    THE HOLE GENERATED"""

    def __init__(self,x,y):

        #position attributes

        self.dsp_x = y
        self.dsp_y = y
    
    @property

    def dsp_x(self):
        return self.__dsp_x

    @dsp_x.setter

    def dsp_x(self, dsp_x):
        self.__dsp_x = dsp_x
    
    @property

    def dsp_y(self):
        return self.__dsp_y

    @dsp_y.setter

    def dsp_y(self, dsp_y):
        self.__dsp_y = dsp_y