# Tkairo_package


# tkairo

A utility library for shortening Tkinter code.

## Installation

```

pip install tkairo

```

## Usage

```python

from tkairo import button, entry, center

button(root, "Click").pack()

entry(root).pack()

center(root) 

```

## Features

- Simplified widget creation

- Simple window management    

- Layout helpers    

- Example themes (without dependencies)

- Thorough testing

- Documentation

## Goals

- Make Tkinter code more readable and concise

- Provide useful utility functions

- Avoid optional dependencies  

- Allow users full flexibility in theming

## Getting Started

See the [documentation](docs/index.md) or [examples](examples).

## Tests

Run tests with:

```

python -m unittest discover

```

## Publishing

1. Bump version in setup.py

2. `python setup.py sdist bdist_wheel`     

3. `twine upload dist/*`

## License

MIT

## Author

Nathan Vilane  

learnfastwithnathan@gmail.com

Hope this helps get you started! The key sections I included are:

- Installation  

- Usage     

- Features    

- Goals

- Getting Started  

- Tests  

- Publishing details

- License

- Author info

You can expand each section with more details as tkairo grows.

Please let me know if you have any other questions or would like me to modify or expand the README in any way. I'm happy to provide more suggestions to help document your library effectively.

Best of luck with tkairo - simplifying Tkinter development is a great goal!
