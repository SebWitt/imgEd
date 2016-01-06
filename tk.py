from sk import imgED
from tkinter import filedialog

def file_dia():
    a = filedialog.askopenfilename()
    img = imgED(a)