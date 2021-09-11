import turtle
import time

wn= turtle.Screen()
wn.title("animation demo")
wn.bgcolor('black')

player=turtle.Turtle()
player.shape('square')
player.color('blue')

while True:
    player.shape('square')
    time.sleep(1)
    player.shape('circle')
    time.sleep(1)

wn.mainloop()