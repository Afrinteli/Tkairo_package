from .widgets import *

from .windows import *   

from .layouts import *

from .themes import *

__all__ = [

    "button",

    "entry",  

    "label",    

    "frame",    

    "center",

    "set_title",

    "set_icon",  

    "grid", 

    "pack",    

    "place",    

    "apply_theme"      

]

__version__ = "0.1.0"

def short_button(master, text, **options):

    btn = button(master, text, **options)        

    return btn

def short_entry(master, text, **options):

    entry = entry(master, **options)

    label(master, text).pack(side="left")

    return entry 
