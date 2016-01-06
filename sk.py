import skimage
import skimage.data
import skimage.io as io
import skimage.filters as filters
import skimage.util as util
import scipy.ndimage as ndimage


class imgED:
    def __init__(self, pic):
        self.img = io.imread(pic)
   
    def show_img(self):
        io.imshow(self.img, "qt")
       
    def filter_gauss(self):
        self.img = ndimage.gaussian_filter(self.img, 1)
    
    def filter_prewitt(self):
        self.img = ndimage.filters.prewitt(self.img)
        
    def refresh_img():
        pass


