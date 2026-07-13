#IMPORTING SASSY LIBS
from SandEngine.Libs import *

# root functions
def visuals():
    pass
def ui():
    pass
def physics():
    pass
def logics():
    pass
def exit():
    pr.close_window()
    sys.exit()

# root

def init_root():
    pr.init_window( 900 , 800 , "SandBoxProject")
    while not pr.window_should_close():
        root()
    else:
        exit()

def root():
    physics()
    logics()
    ui()
    visuals()
