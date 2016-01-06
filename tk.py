import sk
from tkinter import filedialog

def file_dia():
    a = filedialog.askopenfilename()
    sk.read_img(a)
