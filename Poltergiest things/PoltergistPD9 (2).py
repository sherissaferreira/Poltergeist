#Matrix Gaming
 #Polergeist
#James,Sara,Sherissa
#two sentence explanation of the game's objective

from gamelib import*
#objects and initial settings
game = Game (800,600,"kon")
bk = Image("bk.jfif",game)
bk.resizeTo(game.width, game.height)
#leaves=[]
#for index in range(100):
    #leaves.append(Image("gre.png",game))
    #leaves[index].resizeTo(95,95)
    #leaves[index].moveTo(randint(100,600),randint(100,500))
    #leaves[index].setSpeed(0,60)
ora = Image("ora.png",game)
ora.resizeTo(95,95)
kon = Animation("kon.png",16,game,1841/4,2400/4,3)
kon.resizeTo (95, 95)
kon.moveTo (400, 500)
sp = Image("sp.png",game)
sp.resizeTo(180,150)
sp.moveTo(200,500)
de = Animation("de.png",16,game,320/4,320/4,3)
de.resizeTo(180,150)
de.moveTo(550,480)
#if kon.collidedwith(de.png)
#game.over=true
#for index in range(len(bk.xy))
#bk.backgroundxy[i]["x"]+= 150
#The leaves won't work when I run the game 
#Level 1 - game loop


while not game.over:
    game.processInput()
    #game.scrollBackground("left",2)
    bk.draw()
    ora.draw()
    sp.draw()
    kon.draw()
    de.draw()
    game.update(30)

game.over = False
#Level 2 - game loop
while not game.over:
    game.processInput()
    #game.scrollBackground("left",2)
    bk.draw()
    #kon.draw()
    game.update(30)

game.quit()
