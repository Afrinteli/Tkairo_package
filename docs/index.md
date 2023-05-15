# tkairo

A utility library for shortening Tkinter code.

## Installation

Install using pip:

```

pip install tkairo

```

## Usage

Import tkairo:

```python

import tkairo as tkr

```

Create widgets:

```python

btn = tkr.button(root, "Click")  

```  

Center a window:

```python 

tkr.center(root)

```

Use layouts:

```python

frm = tkr.pack_start(Frame(root))  

```

Apply themes:

```python

from tkinter import ttk

style = ttk.Style()

style.theme_use("classic")

tkr.button(root, "Click")  # Automatically themed

```

## API

### Widgets

- tkr.button

- tkr.entry

- tkr.label

- tkr.checkbox  

- ...

### Windows

- tkr.center   

- tkr.set_title

- tkr.set_icon

### Layouts

- tkr.grid  

- tkr.pack_start  

- tkr.pack_end

- tkr.place

This provides:

- Basic installation instructions  

- A usage example  

- Details of the full API  

- Examples of applying themes  

. 
