# skim.py

 Skim.py takes filenames in your current working directory as command line arguments and displays in return the classes and functions used in the file. 

Example:

`> skim foo.py`
    
    ----------------foo.py-------------------
    
    class ClassicClass(object):
        def __init__(self):
        def make_thing_three(thing1, thing2):
    def funk1(arg):
    def funk2(arg, default=Nada):
    def blues():

    ----------------foo.py------------------


## Installation

`> pip install skim.py` 

or to install  development version:

    > git clone https://github.com/mosegontar/skim.py.git`
    > cd skim.py
    > pip install -e .
