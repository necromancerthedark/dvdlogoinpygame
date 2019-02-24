import pygame as pg 

white = (255,255,255)
black = (0,0,0)
pg.init()

height = 1000
width = 700

clock = pg.time.Clock()

dvd = pg.image.load("dvd.png")
dvd2 = pg.image.load("dvd2.png")
window = pg.display.set_mode((height,width))
pg.display.set_caption("DVD")
pg.display.set_icon(dvd)

gameexit = False
x = 400
y = 300
x_shift = 10
y_shift = 10

while not gameexit:
    for events in pg.event.get():
        if events.type == pg.QUIT:
            gameexit = True

    
    x= x+x_shift
    y = y + y_shift

    if x+40>= height or x<=0:
        window.blit(dvd2,(x,y))
        x_shift = -x_shift
    if y+40 >= width or y<=0:
        y_shift = -y_shift
        window.blit(dvd2,(x,y))
    window.fill(white)
    #pg.draw.rect(window,black,[x,y,40,40])
    window.blit(dvd,(x,y))
    clock.tick(10)
    pg.display.update()