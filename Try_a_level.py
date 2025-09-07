import random
from Animation import anim, Trader_animation, living_armor_run_animation,ninja_run_animation,ninja_attack_animation
from Items import identify_item,inventory
from Level_prefabs import level1,level0,Travel
import pygame
from Player import Block, camera_group
from Animation import shine_animation,Item_column_animation,living_armor_run_animation,living_armor_idle_animation,wizzard_run_animation,wizzard_attack_animation

scale = 4
projectiles = [[0,0,0,0,2000,2000,"fireball"]]
sprite_sheet2 = pygame.transform.scale(pygame.image.load("new idea.png"),(pygame.image.load("new idea.png").get_width()*2,pygame.image.load("new idea.png").get_height()*2))
transparent_spritesheet = pygame.transform.scale(pygame.image.load("new idea.png"),(pygame.image.load("new idea.png").get_width()*scale,pygame.image.load("new idea.png").get_height()*scale))
transparent_spritesheet.set_alpha(100)
sprite_sheet3 = pygame.transform.scale(pygame.image.load("another idea.png"),(pygame.image.load("another idea.png").get_width()*scale,pygame.image.load("another idea.png").get_height()*scale))

level = ['vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv'
         'v123405650000000000000000111111111111111153535355353535353535535335353535353535353535v',
         'vp00007070000000000000000111111111111111111111111111111111111111111111111111111111111v',
         'v000005655555555555555555111111111111111153535355353535353535535335353535353535353535v',
         'v000000gggggggggggggggggg0000000000000000vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv',
         'v000000gggggggggggggggggg0000000000000000v',
         'v000000gggggggggggggggggg0000000000000000v',
         'v0000000000000000000000000000000000000000v',
         'v0000000000000000000000000000000000000000v',
         'v0000000000000000000000000000000000000000v',
         'v0000000000000000000000000000000000000000v',
         'v0000000000000000000000000000000000000000v',
         'v0000000000000000000000000000000000000000v',
         'v0000000000000s00000000000000000000000000v',
         'v0000000000000000000000000000000000000000v',
         'v0000000000000000000000000000000000000000v',
         'v0000000000000000000000000000000000000000v',
         'v0000000000000000000000000000000000000000v',
         'v0000000000000000000000000000000000000000v',
         'v0000000000000000000000000000000000000000v',
         'v000000000000000000000000000000000000000v',
         'v0000000000000000000000000000000000000000v',
         'v0000000000000000000000000000000000000000v',
         'v0000000000000000000000000000000000000000v',
         'v0000000000000000000000000000000000000000v',
         'v000000000000000000000000000000000000000v',
         'vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv']
level = level1
def Random_spot():
    x = random.randint(0,len(level[0]))
    y = random.randint(0,len(level))
    for i in range(1,3):
            level[y][x+i]= "1"
    for i in range(0,4):
            level[y][x+i] = "1"
            level[y+1][x + i]= "1"
            level[y+2][x + i]= "1"
    for i in range(1,3):
            level[y+3][x+i]= "1"
# Random_spot()
# Objects collision rules:
# Those functions exist to detect collisions on different borders of rect-like objects
def Bottom_collision(x,y,Px,Py,weight,height):
    if x in range(Px,Px+weight) and y in range(Py+height,Py+height+10):
        return False
    else:return True
def Left_collision(x,y,Px,Py,weight,height):
    if x in range(Px-10,Px) and y in range(Py,Py+height):
        return False
    else:return True
def Right_collision(x,y,Px,Py,weight,height):
    if x in range(Px+weight,Px+weight+10) and y in range(Py,Py+height):
        return False
    else:return True
def Top_collision(x,y,Px,Py,weight,height):
    if x in range(Px,Px+weight) and y in range(Py-10,Py):
        return False
    else:return True


def Draw_a_level(screen,sprite_sheet,scale,delta_camx,delta_camy,x,y,wasd,done,stage):
    global level,transparent_spritesheet,level1,level0,Travel
    level = Travel[int(stage)]
    x = x+8*scale
    y = y+16*scale
    revealed = False
    Ready = False
    wasd = [True,True,True,True]
    for i in range(0,len(level)):
        for n in range(0,len(level[i])):
            if n*16*scale+delta_camx in range(-100,600) and i*16*scale+delta_camy in range(-100,600):
                if level[i][n] == '0':
                    screen.blit(sprite_sheet,(n*16*scale+delta_camx,i*16*scale+delta_camy),[0,0,16*scale,16*scale])
                    # Block((n*16*scale,i*16*scale),camera_group,scale)
                if level[i][n] == '1':
                    screen.blit(sprite_sheet,(n*16*scale+delta_camx,i*16*scale+delta_camy),[16*scale,0,16*scale,16*scale])
                if level[i][n] == '2':
                    screen.blit(sprite_sheet,(n*16*scale+delta_camx,i*16*scale+delta_camy),[0,0,16*scale,16*scale])
                    screen.blit(sprite_sheet, (n * 16 * scale+delta_camx, i * 16 * scale+delta_camy), [0, 16*scale, 16 * scale, 16 * scale])
                if level[i][n] == '3':
                    screen.blit(sprite_sheet, (n * 16 * scale+delta_camx, i * 16 * scale+delta_camy), [16*scale, 16 * scale, 16 * scale, 16 * scale])
                if level[i][n] == '4':
                    screen.blit(sprite_sheet,(n*16*scale+delta_camx,i*16*scale+delta_camy),[0,0,16*scale,16*scale])
                    screen.blit(sprite_sheet,(n*16*scale+delta_camx,i*16*scale+delta_camy),[32*scale,0,16*scale,16*scale])
                    screen.blit(sprite_sheet,(n*16*scale+delta_camx,i*16*scale+delta_camy),[160*scale,0,16*scale,16*scale])
                if level[i][n] == '5':
                    screen.blit(sprite_sheet, (n * 16 * scale + delta_camx, i * 16 * scale + delta_camy),
                                [16 * scale, 0, 16 * scale, 16 * scale])
                    if y in range(i*16*scale+delta_camy-32*scale,i*16*scale+delta_camy) and x in range(n*16*scale+delta_camx,n*16*scale+delta_camx+16*scale):
                        screen.blit(transparent_spritesheet,(n*16*scale+delta_camx,i*16*scale+delta_camy-16*scale),[0,64*scale,16*scale,32*scale])
                    else:
                        screen.blit(sprite_sheet,(n*16*scale+delta_camx,i*16*scale+delta_camy-16*scale),[0,64*scale,16*scale,32*scale])
                    # wasd[0] = wasd[0] and Bottom_collision(x,y,n*16*scale+delta_camx,i*16*scale+delta_camy,16*scale,16*scale)
                    # wasd[1] = wasd[1] and Right_collision(x,y,n*16*scale+delta_camx,i*16*scale+delta_camy,16*scale,16*scale)
                    # wasd[2] = wasd[2] and Top_collision(x,y,n*16*scale+delta_camx,i*16*scale+delta_camy,16*scale,16*scale)
                    # wasd[3] = wasd[3] and Left_collision(x,y,n*16*scale+delta_camx,i*16*scale+delta_camy,16*scale,16*scale)
                if level[i][n] == '6':
                    screen.blit(sprite_sheet, (n * 16 * scale + delta_camx, i * 16 * scale + delta_camy),
                                [16 * scale, 0, 16 * scale, 16 * scale])
                    screen.blit(sprite_sheet,(n*16*scale+delta_camx,i*16*scale+delta_camy-16*scale),[16*scale,64*scale,16*scale,32*scale])
                if level[i][n] == '7':
                    screen.blit(sprite_sheet, (n * 16 * scale + delta_camx, i * 16 * scale + delta_camy),
                                [16 * scale, 0, 16 * scale, 16 * scale])
                    screen.blit(sprite_sheet,(n*16*scale+delta_camx,i*16*scale+delta_camy-16*scale),[16*scale,96*scale,16*scale,32*scale])
                if level[i][n] == 'g':
                    screen.blit(sprite_sheet, (n * 16 * scale + delta_camx, i * 16 * scale + delta_camy),
                                [0, 0, 16 * scale, 16 * scale])
                    screen.blit(sprite_sheet, (n * 16 * scale + delta_camx, i * 16 * scale + delta_camy-8*scale),
                                [0, 128*scale, 16 * scale, 16 * scale])
                if level[i][n] == 'p':
                    if done == True:
                        screen.blit(sprite_sheet, (n * 16 * scale + delta_camx, i * 16 * scale + delta_camy),
                                    [0, 0, 16 * scale, 16 * scale])
                        screen.blit(sprite_sheet, (n * 16 * scale + delta_camx-16*scale, i * 16 * scale + delta_camy-16*scale),
                                    [32*scale, 80*scale, 32 * scale, 32 * scale])
                        if x in range(n * 16 * scale + delta_camx-16*scale,n * 16 * scale + delta_camx-16*scale+32*scale) and y in range(i * 16 * scale + delta_camy-16*scale+32*scale):
                            Ready = True
                    else:
                        screen.blit(sprite_sheet, (n * 16 * scale + delta_camx, i * 16 * scale + delta_camy),
                                    [0, 0, 16 * scale, 16 * scale])
                if level[i][n] == 's':
                    screen.blit(sprite_sheet,(n*16*scale+delta_camx,i*16*scale+delta_camy),[16*scale,0,16*scale,16*scale])
                    screen.blit(sprite_sheet,(n*16*scale+delta_camx-16*scale,i*16*scale+delta_camy),[64*scale,112*scale,32*scale,16*scale])
                if level[i][n] == 'S':
                    screen.blit(sprite_sheet, (n * 16 * scale + delta_camx, i * 16 * scale + delta_camy),
                                [0 * scale, 0, 16 * scale, 16 * scale])
                    screen.blit(sprite_sheet, (n*16*scale+delta_camx-16*scale,i*16*scale+delta_camy),
                                [64 * scale, 128 * scale, 32 * scale, 16 * scale])
                if level[i][n] == 'n':
                    screen.blit(sprite_sheet,(n*16*scale+delta_camx,i*16*scale+delta_camy),[16*scale,0,16*scale,16*scale])
                    screen.blit(sprite_sheet,(n*16*scale+delta_camx-16*scale,i*16*scale+delta_camy),[64*scale,112*scale,32*scale,16*scale])
                if level[i][n] == 'N':
                    screen.blit(sprite_sheet, (n * 16 * scale + delta_camx, i * 16 * scale + delta_camy),
                                [0 * scale, 0, 16 * scale, 16 * scale])
                    screen.blit(sprite_sheet, (n*16*scale+delta_camx-16*scale,i*16*scale+delta_camy),
                                [64 * scale, 144 * scale, 32 * scale, 16 * scale])
                if level[i][n] == "b":
                    screen.blit(sprite_sheet, (n * 16 * scale+delta_camx, i * 16 * scale+delta_camy), [16*scale, 16 * scale, 16 * scale, 16 * scale])

            if level[i][n] == '!':
                    pass
    return Ready
def Check_Collisions(screen,sprite_sheet,scale,delta_camx,delta_camy,x,y,entities):
    global level,transparent_spritesheet
    # This function is responsible for determining collisions of various objects(as casual walls and movestones)
    x = x+8*scale
    y = y+16*scale
    revealed = False
    wasd = [True,True,True,True]
    for i in range(0,len(level)):
        for n in range(0,len(level[i])):
            if n*16*scale+delta_camx in range(-100,600) and i*16*scale+delta_camy in range(-100,600):
                if level[i][n] == '5' or level[i][n] == 'v':
                    wasd[0] =wasd[0] and  Bottom_collision(x,y,n*16*scale+delta_camx,i*16*scale+delta_camy,16*scale,16*scale)
                    wasd[1] = wasd[1] and Right_collision(x,y,n*16*scale+delta_camx,i*16*scale+delta_camy,16*scale,16*scale)
                    wasd[2] = wasd[2] and Top_collision(x,y,n*16*scale+delta_camx,i*16*scale+delta_camy,16*scale,16*scale)
                    wasd[3] = wasd[3] and Left_collision(x,y,n*16*scale+delta_camx,i*16*scale+delta_camy,16*scale,16*scale)
                if level[i][n] == "s":
                    for s in range(0,len(entities)):
                        if entities[s][1]+delta_camx in range(n*16*scale+delta_camx-16*scale,n*16*scale+delta_camx+32*scale) and entities[s][2]+delta_camy in range(i*16*scale+delta_camy,i*16*scale+delta_camy+16*scale) and entities[s][0] == "movestone":
                            level[i] = str(level[i][:n])+'S'+str(level[i][n+1:])
                            print(str(level[i][:n])+'S'+str(level[i][n:]))
                if level[i][n] == "n":
                    for s in range(0,len(entities)):
                        if entities[s][1] + delta_camx in range(n * 16 * scale + delta_camx - 16 * scale,
                                                                n * 16 * scale + delta_camx + 16 * scale) and \
                                entities[s][
                                    2] + delta_camy in range(i * 16 * scale + delta_camy - 16 * scale,
                                                             i * 16 * scale + delta_camy) and entities[s][
                            0] == "movestone":
                            level[i] = str(level[i][:n])+'N'+str(level[i][n+1:])
                            print(str(level[i][:n])+'S'+str(level[i][n:]))

                if level[i][n] == "N":
                    blue = False
                    # passing if there are a movestone on this point, so it becomes blue
                    # but in backs to red one if there are no movestone
                    for s in range(0, len(entities)):
                        if entities[s][1] + delta_camx in range(n * 16 * scale + delta_camx-16*scale,
                                                                    n * 16 * scale + delta_camx + 16 * scale) and entities[s][
                                2] + delta_camy in range(i * 16 * scale + delta_camy-16*scale, i * 16 * scale + delta_camy) and entities[s][0] == "movestone":
                            blue = True
                            break
                    if blue == False:
                        level[i] = str(level[i][:n]) + 'n' + str(level[i][n + 1:])
                if level[i][n] == "b":
                    blue_left = False
                    wasd[0] = wasd[0] and Bottom_collision(x, y, n * 16 * scale + delta_camx,
                                                           i * 16 * scale + delta_camy, 16 * scale, 16 * scale)
                    wasd[1] = wasd[1] and Right_collision(x, y, n * 16 * scale + delta_camx,
                                                          i * 16 * scale + delta_camy, 16 * scale, 16 * scale)
                    wasd[2] = wasd[2] and Top_collision(x, y, n * 16 * scale + delta_camx, i * 16 * scale + delta_camy,
                                                        16 * scale, 16 * scale)
                    wasd[3] = wasd[3] and Left_collision(x, y, n * 16 * scale + delta_camx, i * 16 * scale + delta_camy,
                                                         16 * scale, 16 * scale)

                    for m in range(0,len(level)):
                        if not ('n' in level[m]):
                            pass
                        else:
                            blue_left = True
                    if blue_left == False:
                        level[i] = str(level[i][:n]) + '1' + str(level[i][n + 1:])


                # if level[i][n] == '6':
                #     screen.blit(sprite_sheet, (n * 16 * scale + delta_camx, i * 16 * scale + delta_camy),
                #                 [16 * scale, 0, 16 * scale, 16 * scale])
                #     screen.blit(sprite_sheet,(n*16*scale+delta_camx,i*16*scale+delta_camy-16*scale),[16*scale,64*scale,16*scale,32*scale])
                # if level[i][n] == '7':
                #     screen.blit(sprite_sheet, (n * 16 * scale + delta_camx, i * 16 * scale + delta_camy),
                #                 [16 * scale, 0, 16 * scale, 16 * scale])
                #     screen.blit(sprite_sheet,(n*16*scale+delta_camx,i*16*scale+delta_camy-16*scale),[16*scale,96*scale,16*scale,32*scale])
    return wasd
def fill_entities(lvl,entities):
    # This func is responsible for spawning entities every time player enters a new level
    if lvl == 1:

        # entities.append(["wizzard",900,300,2,0,0,False,300,300,100])
        entities.append(["movestone", 0, 0, 2, 0, 0, False, 300, 300, 0])
        entities.append(["gem", 900, 500, 2, 0, 0, False, 300, 300, 100])
        # entities.append(["ninja", 400, 900, 2, 0, 0, False, 300, 300, 100])
        # entities.append(["living_armor", 900, 900, 2, 0, 0, False, 300, 300, 100])


    if lvl == 2:
        entities.append(["zombie",100,100,2,0,0,False,300,300,100])
        entities.append(["zombie", 900, 100, 2, 0, 0, False, 300, 300, 100])
        entities.append(["zombie", 900, 900, 2, 0, 0, False, 300, 300, 100])
        entities.append(["zombie", 100, 900, 2, 0, 0, False, 300, 300, 100])
        entities.append(["living_armor", 700, 700, 2, 0, 0, False, 300,300,100])
    if lvl == 3:
        entities.append(["zombie",100,100,2,0,0,False,300,300,100])
        entities.append(["zombie", 900, 100, 2, 0, 0, False, 300, 300, 100])
        entities.append(["zombie", 900, 900, 2, 0, 0, False, 300, 300, 100])
        entities.append(["zombie", 100, 900, 2, 0, 0, False, 300, 300, 100])
        entities.append(["living_armor", 700, 700, 2, 0, 0, False, 300,300,100])
def move_the_stone(Px,Py,x,y,step,projectiles):
    # Just a move patterns for a "movestone"
    x = x+8*scale
    y = y+16*scale
    delta_x, delta_y = 0, 0
    if Bottom_collision(x, y, Px, Py, 32 * scale,
                                           32 * scale)==False and step[1]<0:
        delta_y = step[1]
    if Right_collision(x, y, Px, Py, 32 * scale,
                                           32 * scale)==False and step[0]<0:
        delta_x = step[0]
    if Top_collision(x, y, Px, Py, 32 * scale,
                                           32 * scale)==False and step[1]>0:
        delta_y = step[1]
    if Left_collision(x, y, Px, Py, 32 * scale,
                                           32 * scale)==False and step[0]>0:
        delta_x = step[0]


    return delta_x,delta_y
def movestone_collision(Px,Py,x,y,wasd,screen):
    # this func just makes movestones act as a barriers
    # Doesn`t works now.
    wasd[0] = wasd[0] and Bottom_collision(x, y, Px, Py, 32 * scale,
                                           32 * scale)
    rect = pygame.Rect(Px, Py, 32 * scale,
                                           32 * scale)
    pygame.draw.rect(screen, (255, 0, 0), rect)
    wasd[1] = wasd[1] and Right_collision(x, y, Px, Py, 32 * scale,
                                           32 * scale)
    wasd[2] = wasd[2] and Top_collision(x, y, Px, Py, 32 * scale,
                                           32 * scale)
    wasd[3] = wasd[3] and Left_collision(x, y, Px, Py, 32 * scale,
                                           32 * scale)
    return wasd
def heal_aura(Px,Py,entities):
    # heals entities around

    return
def meele(Px,Py,Tarx,Tary,speed):
    # Move pattern for a meele entities

    delta_x,delta_y = 0,0
    if Px < Tarx:
        delta_x+=speed
    if Px > Tarx:
        delta_x-=speed
    if Py < Tary:
        delta_y+=speed
    if Py > Tary:
        delta_y-=speed
    return [delta_x,delta_y]

def entities_itself(entities,x,y,i,k_e,projectiles,step):
    # this func is responsible for all the calculations about entities
    # all this happens on the host.
    cur = entities[i]
    type = cur[0]
    Px,Py = cur[1],cur[2]
    cooldowns = (cur[4],cur[5])
    aggresive = cur[6]
    best = 250
    hp = cur[9]
    target = [Px,Py]
    delta_Px, delta_Py = 0,0
    if x in range(Px-1000,Px+1000) and y in range(Py-1000,Py+1000):
        target = [x, y]

    if hp >0:
        if type == "wizzard":
            if len(projectiles) < 1 and (Px, Py) != (x, y):
                projectiles.append(([Px, Py, Px, Py, x, y, "fireball"]))
            if not (x in range(Px-200,Px+200) and y in range(Py-200,Py+200)):
                delta_Px,delta_Py = meele(Px,Py,target[0],target[1],1)
        if type == "ninja":
            if not (x in range(Px-150,Px+150) and y in range(Py-150,Py+150)):
                delta_Px,delta_Py = meele(Px,Py,target[0],target[1],3)
        if type == "gem":
            if not (x in range(Px-100,Px+100) and y in range(Py-100,Py+100)):
                delta_Px,delta_Py = meele(Px,Py,target[0],target[1],1)
        if type == "zombie":
                delta_Px,delta_Py = meele(Px,Py,target[0],target[1],1)

        if type == "trader":
            delta_Px,delta_Py = meele(Px, Py, target[0], target[1], 0)
            if x in range(Px-400,Px+400) and y in range(Py-400,Py+400):
                aggresive = True
        if type == "living_armor":
            delta_Px,delta_Py = meele(Px,Py,target[0],target[1],2)
        for n in range(0, len(entities)):
            if entities[n][1] in range(Px - 100, Px + 100) and entities[n][2] in range(Py - 100, Py + 100) and \
                    entities[n][0] == "gem":
                if hp<100:
                    hp += 0.1
                else:
                    hp = 100
    else:
        delta_Px,delta_Py = meele(Px,Py,target[0],target[1],0)
        if type == "movestone":
           delta_Px,delta_Py = move_the_stone(Px,Py,x,y,step,projectiles)
           for i in range(0, len(projectiles)):
               if projectiles[i][1] in range(Px, Px + 32 * scale) and projectiles[i][2] in range(Py, Py + 32 * scale):
                       projectiles.pop(projectiles[i])
        if type == "closed" or type == "opened" or type == "looted":
            Loot_chest(Px,Py,x,y,entities[i][0],k_e,entities[i][6])
    print("agressive:",aggresive)
    return delta_Px,delta_Py,best,aggresive,target[0],target[1],projectiles,round(hp,1)
def Loot_chest(Px,Py,x,y,condition,k_e,name):
    # Loot chest logic ...
    # this func detects the interactions with chest
    global scale,sprite_sheet2,inventory
    print(name,condition)
    if condition == "closed":
        doll = [16*scale, 128*scale, 16 * scale, 16 * scale]
        if x in range(Px-200,Px+200) and y in range(Py-200,Py+200):
            condition = "opened"
    if condition == "opened":
        doll = [32 * scale, 128 * scale, 16 * scale, 32 * scale]
        # screen.blit(sprite_sheet2, (Px+16, Py),identify_item(name))
        print("k_e",k_e,type(k_e))
        if k_e == "True":
            condition = "looted"
    if condition == "looted":
        doll = [32 * scale, 128 * scale, 16 * scale, 32 * scale]

    return condition
def Chest_onclient(Px, Py,x,y, screen, sprite_sheet,condition,k_e,name,timer,last_update):
        # Just chest draw logic
        if condition == "closed":
            screen.blit(sprite_sheet,(Px,Py),[16 * scale, 128 * scale, 16 * scale, 16 * scale])
            if x in range(Px - 200, Px + 200) and y in range(Py - 200, Py + 200):
                condition = "opened"
        if condition == "opened":
            screen.blit(sprite_sheet,(Px,Py-16*2),[32 * scale, 128 * scale, 16 * scale, 32 * scale])
            screen.blit(sprite_sheet2, (Px+16, Py),identify_item(name))
            shine_animation(screen,(Px+16, Py))
            if k_e:
                inventory.append(name)
        if condition == "looted":
            screen.blit(sprite_sheet,(Px,Py-16*2),[32 * scale, 128 * scale, 16 * scale, 32 * scale])



def entities_onclient(entities,screen,scale,sprite_sheet,delta_camx,delta_camy,x,y,keys,wasd):
    global sprite_sheet3,projectiles
    # most meaning of this func is to draw correctly all the entities on client
    # and to hand over all the interactions with them to the host
    print(entities,len(entities))
    for i in range(0,len(entities),1):
        # state the vars
        cur = entities[i]
        print(cur,len(entities),i)
        type = cur[0]
        Px,Py = cur[1]+delta_camx,cur[2]+delta_camy
        name = cur[6]
        anim_cd = cur[3]
        tar = (cur[7],cur[8])
        hp = cur[9]
        moving = False
        if tar != (cur[1],cur[2]):
            moving = True
        print(cur[1],cur[2],"sigma",tar)
        if hp>0:
            # visual hp bar
            rect = pygame.Rect(Px - 8 * scale, Py - 80, round(hp), 15)
            pygame.draw.rect(screen, (200, 50, 50), rect)

            if type == "wizzard":
                if moving == True and not (x in range(Px-200,Px+200) and y in range(Py-200,Py+200)):
                    wizzard_run_animation(screen,(Px - 8 * scale, Py - 10 * scale))

                else:
                    screen.blit(sprite_sheet3, (Px - 8 * scale, Py - 10 * scale),
                                [0 * scale, 230 * scale, 17 * scale, 20 * scale])
            if type == "zombie":
                screen.blit(sprite_sheet, (Px-8*scale,Py-10*scale), [32*scale, 16*scale, 16 * scale, 16 * scale])
            if type == "ninja":
                if moving == True:
                    ninja_run_animation(screen,(Px-8*scale,Py-10*scale))
                else:
                    ninja_attack_animation(screen,(Px-8*scale,Py-10*scale))
            if type == "gem":
                screen.blit(sprite_sheet3,(Px-8*scale,Py-10*scale),[128*scale,16*scale,16*scale,16*scale])
            if type == "trader":
                if cur[6] == "True":
                    Item_column_animation(screen,(Px-100,Py-100))
                    Trader_animation(screen,(Px-8*scale,Py-10*scale))
                else:
                    screen.blit(sprite_sheet3, (Px-8*scale,Py-10*scale), [0*scale, 0*scale, 16 * scale, 16 * scale])
            if type == "living_armor":

                if moving == True:

                    living_armor_run_animation(screen,(Px-8*scale,Py-14*scale))

                else:
                    living_armor_idle_animation(screen,(Px-8*scale,Py-14*scale))

        else:
            print(cur[6])
            Chest_onclient(Px, Py,x,y, screen, sprite_sheet,cur[0],keys,cur[6],cur[6][3],cur[6][4])
            if type == "movestone":
                screen.blit(sprite_sheet,(Px,Py),[64*scale,82*scale,32*scale,30*scale])
                # wasd = movestone_collision(Px, Py, x, y, wasd,screen)
    return wasd