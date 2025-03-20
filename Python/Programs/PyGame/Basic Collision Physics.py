import pygame as pg
from pygame.locals import *

pg.init()

h = 1080
w = 1980

win = pg.display.set_mode((w, h))
pg.display.set_caption("Pygame Collisions")

size = 10

hitbox = Rect(w/2-size/2, h/2-size/2, size, size)

ground_u = Rect(0, -h+10, 2*w, h)
ground_d = Rect(0, h-10, 2*w, h)
ground_l = Rect(-w+40, 0, w, 2*h)
ground_r = Rect(w-40, 0, w, 2*h)

e = 0.5

u_x = u_x_or = 20
u_y = u_y_or = 200
gravity = 10

exit = False
end = False
while not exit:
    
    for ev in pg.event.get():
        if ev.type == pg.QUIT:
            exit = True

        if ev.type == pg.KEYDOWN:
            if ev.key == pg.K_ESCAPE:
                exit = True

    pg.time.Clock().tick(60)

    collide_u = pg.Rect.colliderect(ground_u, hitbox)
    collide_d = pg.Rect.colliderect(ground_d, hitbox)
    collide_l = pg.Rect.colliderect(ground_l, hitbox)
    collide_r = pg.Rect.colliderect(ground_r, hitbox)

    if collide_l or collide_r:

        u_x = -e*u_x

        if collide_r: hitbox.right = ground_r.left
        if collide_l: hitbox.left = ground_l.right

    if collide_u:

        hitbox.top = ground_u.bottom
        
        u_y = -e*u_y

    if collide_d:

        hitbox.bottom = ground_d.top
        
        if u_y_or != 0:
            u_y = u_y_or = u_y_or-5
        else:
            end = True

    if not end:

        hitbox.bottom -= u_y
        u_y -= gravity

    hitbox.right += u_x
    
    pg.draw.circle(win, (0, 255, 255), (hitbox.x+size/2, hitbox.y+size/2), size/2)
    #pg.draw.rect(win, (255, 0, 0), hitbox)
    
    pg.draw.rect(win, (0, 255, 255), ground_u)
    pg.draw.rect(win, (0, 255, 255), ground_d)
    pg.draw.rect(win, (0, 255, 255), ground_l)
    pg.draw.rect(win, (0, 255, 255), ground_r)

    pg.display.update()
    win.fill((0, 0, 0))