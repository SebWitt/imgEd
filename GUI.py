from tkinter import *
from tkinter import filedialog
from scipy import misc, ndimage
import PIL
from PIL import ImageTk
import sk
import pseudoStack
import tempfile
from numpy import save

#pseudoStack = [] # <-- Stack!&%"&$"!"§$


# not DAU approved, so care about input
# works best with *.jpg
# *.png gets strange in my case
# dont wonder about attrError, without that error it doenst work
#   can't figure out why
class Toolbar():
    
    def __init__(self, master):
        
        toolFrame = Frame(master)
        toolFrame.grid()
        
        self.scrWidth = root.winfo_screenwidth() # width of the screen
        self.scrHeight = root.winfo_screenheight()
        self.tempDir = tempfile.TemporaryDirectory()
        self.suffix = [] # suffix of file
        
        self.x_resize = Entry(master)
        self.x_resize.grid(row = 3, column = 0)
        
        self.y_resize = Entry(master)
        self.y_resize.grid(row = 4, column = 0)
        
        self.openButton = Button(toolFrame, text = "open", command = self.openImg, width = "13")
        self.openButton.grid(row = 0, column = 0, sticky = "w")
        
        self.saveButton = Button(toolFrame, text = "save as", command = self.saveImg, width = "13")
        #self.saveButton.grid(row = 0, column = 0)
        
        self.resizeButton = Button(toolFrame, text = "resize", command = self.resizeImg, width = "13")
        self.resizeButton.grid(row = 1, column = 0, sticky = "w")
        
        self.test = Button(toolFrame, text = "Change frame size", command = self.chFrame, width = "13")
        self.test.grid(row = 2, column = 0, sticky = "w")
        
        
        
        """
        self.resizeLabelX = Label(toolFrame, text = "x ")
        self.resizeLabelX.grid()
        
        self.resizeLabelY = Label(toolFrame, text = "y ")       
        self.resizeLabelY.grid()
        
        """
        
        self.undoButton = Button(toolFrame, text = "Undo Action", command = self.undo, width = "13")
        self.undoButton.grid(row = 4, column = 0, sticky = "w")
        # how some filter button could look like
        self.gaussButton = Button(toolFrame, text = "Gaussian filter", command = self.gauss, width = "13")
        self.gaussButton.grid(row = 5, column = 0, sticky = "w")
        
        self.flipVButton = Button(toolFrame, text = "Flip (vertical)", command = self.flip_vertical, width = "13")
        self.flipVButton.grid(row = 7, column = 0, sticky = "w")
        
        self.flipHButton = Button(toolFrame, text = "Flip (horizontal)", command = self.flip_horizon, width = "13")
        self.flipHButton.grid(row = 8, column = 0, sticky = "w")
        
        self.invertButton = Button(toolFrame, text = "Invert", command = self.invert, width = "13")
        self.invertButton.grid(row = 9, column = 0, sticky = "w")
        
        self.uniformButton = Button(toolFrame, text = "Uniform", command = self.uniform, width = "13")
        self.uniformButton.grid(row = 10, column = 0, sticky = "w")
        
        self.prewittButton = Button(toolFrame, text = "Prewitt", command = self.prewitt, width = "13") # prewitt !1!!!1!
        self.prewittButton.grid(row = 11, column = 0, sticky = "w")
        
        self.sobelButton = Button(toolFrame, text = "Sobel", command = self.sobel, width = "13")
        self.sobelButton.grid(row = 12, column = 0, sticky = "w")
        
        self.thresholdButton = Button(toolFrame, text = "Threshold", command = self.threshold, width = "13")
        self.thresholdButton.grid(row = 13, column = 0, sticky = "w")
        
        self.normalizeButton = Button(toolFrame, text = "Normalize", command = self.normalize, width = "13")
        self.normalizeButton.grid(row = 14, column = 0, sticky = "w")
        
        self.greyscaleButton = Button(toolFrame, text = "To Greyscale", command = self.greyscale, width = "13")
        self.greyscaleButton.grid(row = 15, column = 0, sticky = "w")
        
        self.fourierButton = Button(toolFrame, text = "Fourier", command = self.fourier, width = "13")
        self.fourierButton.grid(row = 16, column = 0, sticky = "w")
        
        self.plotButton = Button(toolFrame, text = "plot comparison", command = self.plot, width = "13")
        self.plotButton.grid(row = 17, column = 0, sticky = "w")
    
    def plot(self):
    
        sk.io.imshow(pseudoStack.stack[0])
        sk.io.show()
    
    def fourier(self):
    
        name = sk.imgED(pseudoStack.stack[0])
        name.fourier_transformation()
        self.refresh()
        
    def greyscale(self):
        
        name = sk.imgED(pseudoStack.stack[0])
        name.convert_greyscale()
        self.refresh()
    
    def normalize(self):
    
        name = sk.imgED(pseudoStack.stack[0])
        name.normalize()
        self.refresh()
    
    def threshold(self):
    
        name = sk.imgED(pseudoStack.stack[0])
        name.threshold()
        self.refresh()
    
    def sobel(self):
    
        name = sk.imgED(pseudoStack.stack[0])
        name.filter_sobel()
        self.refresh()    
        
    def prewitt(self):
    
        name = sk.imgED(pseudoStack.stack[0])
        name.filter_prewitt()
        self.refresh()    
    
    def uniform(self):
    
        name = sk.imgED(pseudoStack.stack[0])
        name.filter_uniform()
        self.refresh()    
    
    def invert(self):
    
        name = sk.imgED(pseudoStack.stack[0])
        name.invert_img()
        self.refresh()
    
    def flip_horizon(self):
        
        name = sk.imgED(pseudoStack.stack[0])
        name.flip_horizontal()
        self.refresh()    
    
    def flip_vertical(self):
        
        name = sk.imgED(pseudoStack.stack[0])
        name.flip_vertical()
        self.refresh()
    
    def gauss(self):
        
        name = sk.imgED(pseudoStack.stack[0])
        name.filter_gauss()
        self.refresh()
    # the filter button example       
    def resizeImg(self):
        
        x = int(self.x_resize.get())
        y = int(self.y_resize.get())
        imgResized = misc.imresize(pseudoStack.stack[0], (x,y), interp = 'cubic')
        pseudoStack.stack.insert(0, imgResized)
        
        self.chFrame()
        self.refresh()
        
    
    def chFrame(self):
        self.imageWindow.iconify()
        x = self.x_resize.get()
        y = self.y_resize.get()
        self.imageWindow.geometry(x + "x" + y)
        self.imageWindow.deiconify()
    
    def saveImg(self):
    
        path = filedialog.asksaveasfilename()
        if path == '':
            pass
        else:
            misc.imsave(path, pseudoStack.stack[0])
        
    def openImg(self):
        
        
        imgPath = filedialog.askopenfile()
        self.suffix = imgPath.name.split('.')
        self.suffix = self.suffix.pop()
        asArray = ndimage.imread(imgPath.name)
        pseudoStack.stack.insert(0, asArray)
        asPIL = PIL.Image.fromarray(asArray)
        imgWidth = asPIL.size[0]
        imgHeight = asPIL.size[1]
        imgWinPos = "+" + str(int(self.scrWidth / 2) - int(imgWidth / 2)) + "+" + str(int(self.scrHeight / 2) - int(imgHeight / 2))
        self.imageWindow = Toplevel()
        self.imageWindow.protocol("WM_DELETE_WINDOW", start.switchBtn)
        self.saveButton.grid(row = 0, column = 0, sticky = "w")
        self.imageWindow.geometry(imgWinPos)
        forTk = ImageTk.PhotoImage(asPIL)
        self.image = Label(self.imageWindow, image = forTk)
        self.image.grid()
        self.imageWindow.root.update()  
             
   
    def undo(self):
        
        if len(pseudoStack.stack) == 1:
            pass
        else:
            pseudoStack.stack.pop(0)
            self.refresh()
    
        
    def refresh(self):
        forTk = self.convert()
        print(forTk)
        self.image.configure(image = forTk)
        self.image.grid()
        self.imageWindow.root.update()
    
    def convert(self):
        misc.imsave(self.tempDir.name + "temp." + self.suffix, pseudoStack.stack[0]) 
        lame = misc.imread(self.tempDir.name + "temp." + self.suffix)
        asPIL = PIL.Image.fromarray(lame)
        forTk = ImageTk.PhotoImage(asPIL)
        return forTk
    
    def switchBtn(self):
        
        self.saveButton.grid_forget()
        self.imageWindow.destroy()

# ignore the following

root = Tk()
start = Toolbar(root)
w = 145 # width for the Tk root
h = 600 # height for the Tk root


# calculate x and y coordinates for the Tk root window
x = (start.scrWidth/7) - (w/2)
y = (start.scrHeight/2) - (h/2)

# set the dimensions of the screen 
# and where it is placed
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
root.title('Tools')
root.update()

root.mainloop()
