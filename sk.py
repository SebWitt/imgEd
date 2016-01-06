import skimage.io as io
import scipy.ndimage as ndimage
import numpy as np


class imgED:
    def __init__(self, pic):
        self.img = io.imread(pic)
   
    def show_img(self):
        io.imshow(self.img, "qt")
       
    def filter_gauss(self):
        self.img = ndimage.gaussian_filter(self.img, 1)
    
    def filter_prewitt(self):
        self.img = ndimage.filters.prewitt(self.img)
        
    def invert_img(self):
        self.img = np.invert(self.img)
    
    def convert_greyscale(self):
        pass
        
    def refresh_img():
        pass


