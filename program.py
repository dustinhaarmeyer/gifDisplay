import pyglet
from time import sleep
from multiprocessing import Process

sprite1 = pyglet.sprite.Sprite(pyglet.resource.image("bsp.png"))
sprite2 = pyglet.sprite.Sprite(pyglet.resource.image('bsp.png'))
window = pyglet.window.Window(fullscreen=True, visible=True)
showing = 1

@window.event
def on_draw():
    window.clear()
    if showing == 1:
        print("showing == 1")
        sprite1.draw()
    else:
        print("showing == 2")
        sprite2.draw()

def appRun(name): 
    pyglet.app.run()
    print('Run app')

def loadGif(num):
    global sprite1
    global sprite2
    if num == 1:
        print("loadGif(1)")
        sprite1 = pyglet.sprite.Sprite(pyglet.resource.animation('download.gif'))
    elif num == 2:
        print("loadGif(2)")
        sprite1 = pyglet.sprite.Sprite(pyglet.resource.animation('download.gif'))
    else:
        print('Sprite not avaible!! Critical Error')

windowProcess = Process(target=appRun, args=('bob',))

if __name__ == '__main__':
    loadGif(1)
    windowProcess.start()
    sleep(3)
    loadGif(2)