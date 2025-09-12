import pygame
import sys
pygame.init()
scale = 4
interface = pygame.image.load("interface.png")
interface = pygame.transform.scale(interface,(interface.get_width()*scale,interface.get_height()*scale))
# init font
font = pygame.font.Font('PressStart2P-Regular.ttf',18)
# choose area
logo = interface.subsurface((0,32*scale,64*scale,32*scale))
button = interface.subsurface((0,64*scale,64*scale,16*scale))
input = interface.subsurface((0,16*scale,64*scale,16*scale))
small_button = interface.subsurface((0,80*scale,16*scale,16*scale))
# screen = pygame.display.set_mode((600,600))
# choose icons areas
sounds = interface.subsurface((16*scale,80*scale,16*scale,16*scale))
play = interface.subsurface((32*scale,80*scale,16*scale,16*scale))
exit = interface.subsurface((48*scale,80*scale,16*scale,16*scale))
settings = interface.subsurface((16*scale,96*scale,16*scale,16*scale))
bestiary = interface.subsurface((0*scale,96*scale,16*scale,16*scale))
none = interface.subsurface((0*scale,160*scale,16*scale,16*scale))

hp_bar = interface.subsurface((16*scale,0*scale,25*scale,6*scale))
ip_input = '26.247.173.52'
# deafault button func
def Player_hpbar(screen,Health):
    text = font.render(str(Health),1,(255,255,255))
    screen.blit(text,(0,0))
def Button(screen,pos,icon,text,mouse_pos,lmb):
    global button,scale
    # draw button itself and text than
    screen.blit(button,pos)
    text = font.render(text,1,(255,255,255))
    screen.blit(text,(pos[0]+55,pos[1]+15))
    screen.blit(icon,pos)
    # we detect the collision of mouse and the button first
    # then we check if lmb True
    done = False
    if mouse_pos[0] in range(pos[0],pos[0]+64*scale) and mouse_pos[1] in range(pos[1],pos[1]+16*scale):
        if lmb == True:
            done = True
    return done
def Input_win(pos,screen,ip):
    global ip_input,input

    text = font.render(ip,1,(255,255,255))
    screen.blit(input, pos)
    screen.blit(text, pos)
# small button func
def Small_button(screen,pos,icon,text,mouse_pos,lmb):
    global button, scale,small_button
    screen.blit(small_button,pos)
    # same as a button
    done = False
    if mouse_pos[0] in range(pos[0], pos[0] + 64 * scale) and mouse_pos[1] in range(pos[1], pos[1] + 16 * scale):
        if lmb == True:
            done = True
    return done
def menu(screen,mouse_pos,lmb):
    global logo,button,small_button
    screen.blit(logo,(0,0))
    if Button(screen,(0,200),play,"Play",mouse_pos,lmb) ==True:
        return "Play"
    if Button(screen, (0, 300), bestiary, "Bestiary", mouse_pos, lmb) == True:
        return "Bestiary"
    if Button(screen, (0, 400), settings, "Settings", mouse_pos, lmb) == True:
        return "Settings"
    if Button(screen, (0,500),exit,"Exit", mouse_pos, lmb) == True:
        return "Exit"
def Pause_menu(screen,mouse_pos,lmb):
    rect = pygame.Rect(0,200,600,265)
    pygame.draw.rect(screen,(0,0,0),rect)
    Button(screen, (0, 200), play, "Return", mouse_pos, lmb)
    Button(screen, (0, 300), settings, "Settings", mouse_pos, lmb)
    Button(screen, (0,400),exit,"Main menu", mouse_pos, lmb)
    text = font.render("The game is",1,(255,255,255))
    screen.blit(text,(275,225))
    text = font.render("not on pause",1,(255,255,255))
    screen.blit(text,(275,242))
def Saves():
    pass
def IP_input():
    pass
def Create_save(screen,event,mouse_pos,lmb):
    Input_win((0,0),screen,event)
    if Button(screen, (0,500),exit,"Enter", mouse_pos, lmb) == True:
        return "Enter"
    print(True)
