import pgzrun,random
WIDTH=600
HEIGHT=600
TITLE="Bird Day"
score=0
bee=Actor('bee',(300,300))
flower=Actor('flower')
game_over=False

def placeflower():
    flower.x=random.randint(70,WIDTH-70)
    flower.y=random.randint(70,HEIGHT-70)
def time_up():
    global game_over
    game_over=True



def draw():
    screen.clear()
    screen.blit('background',(0,0))
    flower.draw()
    bee.draw()
    screen.draw.text("Score is :" +str(score),color="black",topleft=(10,10))
    if game_over:
        screen.fill("pink")
        screen.draw.text("Times up!Your final score is:"+str(score),midtop=(300,10),fontsize=40,color="red")
    
def update():
    global score
    if keyboard.left:
        bee.x=bee.x-2
        if bee.x<0:
           bee.x=10
    if keyboard.right:
        bee.x=bee.x+2
        if bee.x>600:
           bee.x=590
    if keyboard.down:
        bee.y=bee.y+2
        if bee.y>600:
           bee.y=590
    if keyboard.up:
        bee.y=bee.y-2
        if bee.y<0:
           bee.y=10
    if bee.colliderect(flower):
        score+=10
        placeflower()






clock.schedule(time_up,40.0)
pgzrun.go()