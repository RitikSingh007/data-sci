import pgzrun


music.play('bgm')

b = Actor('icecream1', (250,300))
vx , vy  = 3, 2

def draw():
    screen.fill('white')
    b.draw()

def update(): 
    global vx , vy 
    b.x += vx 
    b.y += vy
    if b.right > 800 or b.left < 0:
        vx = - vx
    if b.bottom > 600 or b.top < 0 :
        vy = - vy 

pgzrun.go()



#sound.s1.play()
#visit pyzero website .....