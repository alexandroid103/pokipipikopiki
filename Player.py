import pygame
import math
from Animation import character_run_animation


# num = 1
# num of the player for multiplayer
# start_position
doll = [32, 0, 16, 16]
Cursor = [128,0,16,16]
# camera_group =  pygame.sprite.Group()

scale =4
sprite_sheet = pygame.transform.scale(pygame.image.load("new idea.png"),(pygame.image.load("new idea.png").get_width()*scale,pygame.image.load("new idea.png").get_height()*scale))
sprite_sheet_second = pygame.transform.scale(pygame.image.load("another idea.png"),(pygame.image.load("another idea.png").get_width()*scale,pygame.image.load("another idea.png").get_height()*scale))

flipped_sprite_sheet = pygame.transform.flip(sprite_sheet,1,0)
player_sprite = sprite_sheet.subsurface((doll[0] * scale, doll[1] * scale, doll[2] * scale, doll[3] * scale))
fireball = sprite_sheet_second.subsurface((5 * scale, 276 * scale, 5 * scale, 5 * scale))

def projectile_damage(screen,projectiles,delta_camx,delta_camy,x,y):
    pass
def projectile(screen,projectiles,delta_camx,delta_camy):
    for i in range(0,len(projectiles)):
        try:
            self_pos = projectiles[i][0], projectiles[i][1]
            start_pos = projectiles[i][2],projectiles[i][3]
            end_pos = projectiles[i][4],projectiles[i][5]
            x_dist =  end_pos[0]-start_pos[0]
            y_dist = end_pos[1]-start_pos[1]
            angle = math.degrees(math.atan2(y_dist,x_dist))
            x_move = math.cos(math.radians(angle)) * projectile_identify(projectiles[i][6])[1]
            y_move = math.sin(math.radians(angle)) * projectile_identify(projectiles[i][6])[1]
            range_dist = projectile_identify(projectiles[i][6])[2]
            if start_pos[0] < end_pos[0]:
                projectiles[i][0]+=x_move
                projectiles[i][1]+=y_move
            if start_pos[0] > end_pos[0]:
                projectiles[i][0]+=x_move
                projectiles[i][1]+=y_move
            x_dist = self_pos[0] - start_pos[0]
            y_dist = self_pos[1] - start_pos[1]
            if x_dist**2+y_dist**2>=range_dist**2:
                projectiles.pop(i)

            print("friend",x_dist**2+y_dist**2)
        except:pass
    print("kaif",len(projectiles))
def draw_projectile(screen,projectiles,delta_camx,delta_camy):
    for i in range(0,len(projectiles)):
        try:
            self_pos = projectiles[i][0], projectiles[i][1]
            start_pos = projectiles[i][2], projectiles[i][3]
            end_pos = projectiles[i][4], projectiles[i][5]
            x_dist = end_pos[0] - start_pos[0]
            y_dist = end_pos[1] - start_pos[1]
            angle = math.degrees(math.atan2(y_dist, x_dist))
            sprite = pygame.transform.rotate(projectile_identify("fireball")[0], int(angle))

            turret = sprite.get_rect(center=(self_pos[0] + (5 * scale)+delta_camx, self_pos[1] + (15 * scale)+delta_camy))
            screen.blit(sprite, turret)
        except:pass
def projectile_identify(type):
    # just identify the projectile`s behaivor connected to whats projectile type is it.
    global fireball
    result = fireball, 5
    if type=="fireball":
        result = fireball,5,1000
    return result
def Control(keys, wasd, speed):
    global x, y
    # just hand over move offset connected to what buttons are pressed
    delta_x = '0'
    delta_y = '0'
    if keys[pygame.K_w] and wasd[0] == True:
        delta_y = '-5'
    if keys[pygame.K_a] and wasd[1] == True:
        delta_x = '-5'
    if keys[pygame.K_s] and wasd[2] == True:
        delta_y = '5'
    if keys[pygame.K_d] and wasd[3] == True:
        delta_x = '5'
    return str(int(delta_x)) + ' ' + str(int(delta_y))+' '


def Draw_Person(spritesheet, screen, scale, x, y,charge,Cx):
    global doll,sprite_sheet,flipped_sprite_sheet,player_sprite
    # Draws a player
    if Cx>=x:
        screen.blit(player_sprite, (x, y))
    else:
        screen.blit(pygame.transform.flip(player_sprite,1,0), (x, y))
    rect = pygame.Rect(x - 8 * scale, y - 80, charge, 15)
    pygame.draw.rect(screen, (60, 179, 113), rect)
    screen.set_at((x,y),(255,0,0))
def Draw_cursor(spritesheet,screen,scale,x,y):
    global Cursor
    screen.blit(spritesheet, (x-8*scale, y-8*scale), [Cursor[0] * scale, Cursor[1] * scale, Cursor[2] * scale, Cursor[3] * scale])
    screen.set_at((x,y),(255,0,0))
def Draw_weapon_packed(screen,lbm,x,y,strenght):
    global sprite_sheet
    if lbm == False and strenght ==0:
        weapon = sprite_sheet.subsurface((112 * scale, 0, 16 * scale, 23 * scale))
        screen.blit(weapon,(x,y-50))
def Draw_weapon(spritesheet,screen,scale,x,y,Cx,Cy,degree,lbm,strenght):
    x_dist = round(Cx-x)
    y_dist = round(-(Cy-y))
    angle = math.degrees(math.atan2(y_dist, x_dist))
    tan = math.tan(math.radians(angle))
    weapon = spritesheet.subsurface((112*scale,0,16*scale,23*scale))
    weapon = pygame.transform.rotate(weapon, angle + degree)
    turret = weapon.get_rect(center=(x + (16 * scale) // 2, y  + (25 * scale) // 2-10))
    screen.blit(weapon, turret)

    # Weapon((x,y),camera_group,scale,Cx,Cy,degree)
def Make_a_hit(degree,phase):
    done = False
    dmg = False
    speed = 4
    if phase == 1:
        if degree == 90:
            dmg = True
        degree-=speed
        if degree <= 10:
            phase =2
    if phase ==2:
        degree+=speed
        if degree>=170:
            phase = 3
    if phase ==3:
        degree-=speed
        if degree ==90:
            dmg = True
            phase = 0
            done = True
    return degree,phase,done,dmg