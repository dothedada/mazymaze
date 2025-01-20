import os

os.environ["XDG_SESSION_TYPE"] = "x11"
from window import Window

win = Window(600, 800)
win.wait_for_close()
