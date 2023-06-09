import setuptools

with open("README.md", "r") as fh:

    long_description = fh.read()

setuptools.setup(

    name="tkairo",  

    version="0.1.0",

    author="Nathan Vilane",

    author_email="learnfastwithnathan@gmail.com",

    description="A utility module to shorten Tkinter code",

    long_description=long_description,  

    long_description_content_type="text/markdown",    

    url="https://github.com/Afrinteli/Tkairo_package",    

    packages=setuptools.find_packages(),  

    install_requires=[],  

    classifiers=[

        "Programming Language :: Python :: 3",

        "License :: OSI Approved :: MIT License",

        "Operating System :: OS Independent",  

    ],

    python_requires='>=3.6'

)
