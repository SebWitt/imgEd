import skimage
import skimage.data
import skimage.io as io
import skimage.filters as filters
import skimage.util as util


img_stack = []
img = ""

def read_img(pic):
    global img
    img = util.img_as_float(io.imread(pic))
    show_img()
    
def show_img():
    global img
    io.imshow(img, "qt")

def refresh_img():
    pass

def undo_change():
    pass

