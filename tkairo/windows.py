from tkinter import *

def center(root):    

    root.update_idletasks()    

    width = root.winfo_width()

    height = root.winfo_height()    

    screen_width = root.winfo_screenwidth()

    screen_height = root.winfo_screenheight()  

        

    x = (screen_width/2) - (width/2)

    y = (screen_height/2) - (height/2)

    root.geometry(f"{width}x{height}+{int(x)}+{int(y)}")

def set_title(root, title):

    root.title(title)

    

def set_icon(root, icon_file):            

    root.iconbitmap(icon_file)
