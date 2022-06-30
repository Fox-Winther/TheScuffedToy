from ursina import *
from time import sleep
import elements

app = Ursina()
window.color = color.black
eleMenuShow = False

window.windowed_size = (640, 480)
window.fullscreen_size = window.windowed_size
window.title = 'The Scuffed Powder'
window.borderless = False
window.fullscreen = True
window.exit_button.visible = False
window.fps_counter.enabled = True

class elementsButton(Button): # a class for all menu entries
    def __init__(self):
        super().__init__(
            radius = 0,
            scale = Vec2(.1, .1),
            position = Vec2(-0,0),
            color = color.gray,
            always_on_top = True
            )

def toggleBool():
    global eleMenuShow
    if eleMenuShow == True:
        eleMenuShow = False
    else:
        eleMenuShow = True
    elementsMenu.enabled=eleMenuShow

elementsMenuButton = Button("Elements", color=color.black, radius=0, highlight_color=color.white, text_color=color.white, scale=Vec2(.1225, .035), position=Vec2(-0.83, 0.483))
elementNIron = elementsButton()
elementsMenuButton.on_click = toggleBool
elementsMenu = Entity(color=color.white, model='quad', scale=Vec2(10,2.5), position=Vec2(-1.3, 2.846), enabled=eleMenuShow)



# def update():


def input(key):
    if key == 'q':
        application.quit
        quit(0)

app.run()
