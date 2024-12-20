import sys
import time

from pygame import *
size=w,h=640,480
display.set_caption('Roger Rabbit🐇')
window=window=display.set_mode(size)
FPS=time.Clock()
colors=(0,52,0)
window.fill(colors)
display.update()
FPS.tick(60)
init()
while True:
    for e in event.get():
        if e.type==QUIT:
            sys.exit()