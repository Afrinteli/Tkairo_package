def grid(master, row, column, **options):   

    widget = Frame(master)       

    widget.grid(row=row, column=column, **options)     

    return widget

def pack_start(widget, **options):   

    widget.pack(**options)      

    return widget

def pack_end(widget, **options):

    widget.pack(side="right", **options)

    return widget

def place(widget, x=0, y=0, **options):

    widget.place(x=x, y=y, **options)

    return widget
