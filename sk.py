import skimage.io as io
import skimage.color as color
import skimage.filter as filters
from skimage import exposure
import scipy.ndimage as ndimage
import scipy.misc as misc
from scipy import fftpack
import numpy as np
import pseudoStack

class imgED:
    def __init__(self, pic):
        if type(pic) is str:
            self.img = io.imread(pic)
        else:
            self.img = pic
   
    def show_img(self):
        io.imshow(self.img, "qt")
       
    def filter_gauss(self):
        self.img = ndimage.gaussian_filter(self.img, 1)
        pseudoStack.stack.insert(0, self.img) 
        
    def filter_uniform(self, size = 10): # needs input of size
        self.img = ndimage.filters.uniform_filter1d(self.img, size)
    
    def filter_prewitt(self):
        self.img = ndimage.filters.prewitt(self.img)
        
    def filter_sobel(self):
        self.img = ndimage.filters.sobel(self.img)
        
    def threshold(self):
        val = filters.threshold_otsu(self.img)
        self.img = self.img < val
        
    def normalize(self):
        p2, p98 = np.percentile(self.img, (2, 98))
        self.img = exposure.rescale_intensity(self.img, in_range = (p2, p98))
        
    def invert_img(self):
        self.img = np.invert(self.img)
    
    def convert_greyscale(self):
        self.img = color.rgb2grey(self.img)
        
    def fourier_transformation(self):
        self.img = np.fft.fft(self.img)
        self.img = np.fft.fftshift(self.img)
        
    def flip_vertical(self):
        self.img = np.fliplr(self.img)
        pseudoStack.stack.insert(0, self.img) 
        
    def flip_horizontal(self):
        self.img = np.flipud(self.img)
        pseudoStack.stack.insert(0, self.img)
    
        
    def refresh_img():
        pass


