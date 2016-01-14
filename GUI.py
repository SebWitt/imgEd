from tkinter import *
from tkinter import filedialog
from scipy import misc
import PIL
from PIL import ImageTk
import sk
import pseudoStack

#pseudoStack = [] # <-- Stack!&%"&$"!"§$


# not DAU approved, so care about input
# works best with *.jpg
# *.png gets strange in my case
# dont wonder about attrError, without that error it doenst work
#   can't figure out why
class Toolbar:
    
    def __init__(self, master):
        
        toolFrame = Frame(master)
        toolFrame.pack()#(row = 1, column = 1)
        
        self.openButton = Button(toolFrame, text = "open", command = self.openImg)
        self.openButton.pack()
        
        self.saveButton = Button(toolFrame, text = "save as", command = self.saveImg)
        self.saveButton.pack()
        
        # how some filter button could look like
        self.resizeButton = Button(toolFrame, text = "resize", command = self.resizeImg)
        self.resizeButton.pack()#(row = 2, column = 2)
        
        self.test = Button(toolFrame, text = "Change frame size", command = self.test)
        self.test.pack()
        
        self.x_resize = Entry(master)
        self.y_resize = Entry(master)
        
        self.resizeLabelX = Label(toolFrame, text = "x ")
        self.resizeLabelX.pack()
        self.x_resize.pack()
        self.resizeLabelY = Label(toolFrame, text = "y ")       
        self.resizeLabelY.pack()
        self.y_resize.pack()
        
        self.undoButton = Button(toolFrame, text = "Undo Action", command = self.undo)
        self.undoButton.pack()
        
        self.gaussButton = Button(toolFrame, text = "Gaussian filter", command = self.gauss)
        self.gaussButton.pack()
        
        self.flipVButton = Button(toolFrame, text = "Flip (vert)", command = self.flip_vertical)
        self.flipVButton.pack()
        
        self.flipHButton = Button(toolFrame, text = "Flip (horizontal)", command = self.flip_horizon)
        self.flipHButton.pack()
        
    
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
        self.refresh()
    
    def test(self):
        x = self.x_resize.get()
        y = self.y_resize.get()
        self.imageWindow.geometry(x + "x" + y)
    
    def saveImg(self):
    
        path = filedialog.asksaveasfilename()
        misc.imsave(path, pseudoStack.stack[0])
        
    def openImg(self):
        
        
        imgPath = filedialog.askopenfile()
        asArray = misc.imread(imgPath.name)
        pseudoStack.stack.insert(0, asArray)
        asPIL = PIL.Image.fromarray(asArray)
        
        self.imageWindow = Toplevel()
        forTk = ImageTk.PhotoImage(asPIL)
        self.image = Label(self.imageWindow, image = forTk)
        self.image.pack()
        self.imageWindow.root.update()  
             
   
    def undo(self):
        pseudoStack.stack.pop(0)
        self.refresh()
    
        
    def refresh(self):
        forTk = self.convert()
        self.image.configure(image = forTk)
        self.image.pack()
        self.imageWindow.root.update()
    
    def convert(self):
        asPIL = PIL.Image.fromarray(pseudoStack.stack[0])
        forTk = ImageTk.PhotoImage(asPIL)
        return forTk

# ignore the following

root = Tk()
start = Toolbar(root)
w = 120 # width for the Tk root
h = 300 # height for the Tk root

# get screen width and height
ws = root.winfo_screenwidth() # width of the screen
hs = root.winfo_screenheight() # height of the screen

# calculate x and y coordinates for the Tk root window
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

# set the dimensions of the screen 
# and where it is placed
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
root.update()
root.mainloop()
