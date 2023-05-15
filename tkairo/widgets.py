from tkinter import *

def button(master, text, **options): 

    btn = Button(master) 

    btn["text"] = text   

    for key, value in options.items():

        btn[key] = value

    return btn

def entry(master, **options):   

    ent = Entry(master, **options) 

    return ent

def label(master, text, **options):   

    lab = Label(master, text=text, **options)    

    return lab 

def checkbox(master, text, **options):

    cb = Checkbutton(master, text=text, **options)    

    return cb

def frame(master, **options):

    frm = Frame(master, **options)    

    return frm    

    

# Add more widget functions... 
