import pyglet
from time import sleep
from multiprocessing import Process

sprite = pyglet.sprite.Sprite(pyglet.resource.animation('download.gif'))
window = pyglet.window.Window(fullscreen=True, visible=True)
#pyglet.gl.glClearColor(1, 1, 1, 1)

@window.event
def on_draw():
    window.clear()
    sprite.draw()

def appRun(name): #umdrehen: Fenster läuft normal. 2.Prozess wartet auf nächstes Bild und ändert Variable zu Bild-Pfad
    #while... sleep
    pyglet.app.run()
    print('Run app')

p = Process(target=appRun, args=('bob',))

if __name__ == '__main__':
    p.start()
    #p.join()
    sleep(3)
    print('Started Window')
print("2")