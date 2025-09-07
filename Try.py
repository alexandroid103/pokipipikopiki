import pygame
import sys
import socket
import pyperclip
from Player import Control,Draw_Person,Draw_cursor,Draw_weapon,Make_a_hit,camera_group,Draw_weapon_packed,projectile,draw_projectile
from Try_a_level import Draw_a_level,entities_onclient,Check_Collisions,projectiles
from test import Decode_Data
from Items import Draw_inventory
from Animation import character_run_animation
from Menu import menu, Pause_menu, Create_save, ip_input
import time

pygame.init()
#инициируем пайгейм
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
sock.setsockopt(socket.IPPROTO_TCP,socket.TCP_NODELAY,1)
# этот сокет остается блокирующим чтобы лищний раз не отправлять данные на сервер и работал с такой же частотой
# sock.connect(('192.168.0.161',10000))
# sock.connect(('26.247.173.52',10000))
# server_num = sock.recv(1024)
# print(server_num)
# sock.connect(('37.195.89.59',10000))
# init client_socket
scale = 4
# init scale
sprite_sheet = pygame.transform.scale(pygame.image.load("new idea.png"),(pygame.image.load("new idea.png").get_width()*scale,pygame.image.load("new idea.png").get_height()*scale))
# creating a new spritesheet
screen = pygame.display.set_mode((600,600))


# creating a new display
background_color = (255,255,255)
# init background_color
wasd = [True,True,True,True]
speed = 3
# shows the possibility to move andd speed) obviously
stage = 0
# to make hits
hit = [90,1]
charge = 0
delta_camx,delta_camy = 0,0
# scene conditions
scene = "menu"
pause = False
connection = False
last_data = 0
while True:
    k_e = False
    screen.fill(background_color)
    keys = pygame.key.get_pressed()
    # sock.connect((ip_input, 10000))
    print(scene)

    # Starts a main cicle
    for event in pygame.event.get():
        key_type = event.type
        if event.type == pygame.QUIT:
            sys.exit()
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if scene == "choise":
                if event.key == pygame.K_BACKSPACE and len(ip_input)>=1:
                    ip_input = ip_input[:-1]
                elif len(ip_input)<13:
                    if pygame.key.get_mods() and pygame.KMOD_CTRL and event.key == pygame.K_v:
                        ip_input +=pyperclip.paste()
                    else:
                        ip_input += event.unicode

        if event.type == pygame.KEYUP :
            if event.key == pygame.K_e:
                k_e = True
            if event.key == pygame.K_ESCAPE:
                if pause == False:
                    pause = True
                elif pause == True:
                    pause = False
    cursor = pygame.mouse.get_pos()
    lmb = pygame.mouse.get_pressed(3)
    pos = Control(keys, wasd, speed)

    dmg = False
    if scene == "menu":
        background_color = (0,0,0)
        menu_result =menu(screen,cursor,lmb[0])
        if  menu_result =="Play":
            scene = "choise"
    if scene == "choise":

        background_color = (0, 0, 0)
        menu_result = Create_save(screen,ip_input,cursor,lmb[0])
        if menu_result == "Enter":

            if len(ip_input) == 13:
                sock.connect((ip_input, 10000))
                ip_input = ''
            try:
                data = sock.recv(1024)
                data = data.decode()
                if data != "0":
                    scene = "game"

            except:pass
    if scene == "game":
        pygame.mouse.set_visible(False)
        background_color = (255, 255, 255)
        if lmb[0] == True:
            if charge<20:
                charge+=1
        else:
            if hit[1] == 0:
                charge = 0

        data = sock.recv(1024)
        data = data.decode()
        print("skibidi",data)
        try:
            Players,Entities,Queue,Next,stage,Projectiles = Decode_Data(data)
            delta_camx -= int(pos.split(" ")[0])
            delta_camy -= int(pos.split(" ")[1])
        except:pass
        # data1 =sock.recv
        # data1 = data1.decode()
        done = True
        for i in range(0,len(Entities)):
            if Entities[i][9]>0:
                done = False
        # if Next == "True" and done == True:
        #     print("ДА")
        #     stage+=1
        # Next = "False"
        wasd = Check_Collisions(screen, sprite_sheet, scale, delta_camx, delta_camy, 300, 300,Entities)

        Ready = Draw_a_level(screen, sprite_sheet, scale, delta_camx, delta_camy, 300, 300, wasd,done,stage)


        for i in range(0,len(Players)):
            try:
                x,y = Players[i][0],Players[i][1]
                Cx, Cy = Players[i][5], Players[i][6]
                if i == Queue:
                    delta_camx = -x+300
                    delta_camy = -y+300
                    print((x+delta_camx,y+delta_camy))
                    # Draw_weapon_packed(screen,lmb[0],300,300,charge)
                    if int(pos.split(" ")[0]) ==0 and int(pos.split(" ")[1]) == 0:
                        Draw_Person(sprite_sheet, screen, scale, x+delta_camx,y+delta_camy, charge, Cx)
                        # Draw_Person(sprite_sheet, screen, scale, 300, 300, charge, Cx)
                        # Draw_Person(sprite_sheet, screen, scale, 300, 300, charge, Cx)
                    else:
                        character_run_animation(screen,(x+delta_camx,y+delta_camy),Cx)
                    Draw_cursor(sprite_sheet, screen, scale, Cx, Cy)
                    Draw_weapon(sprite_sheet, screen, scale, 300, 300, Cx, Cy, hit[0],lmb[0],charge)

                    if lmb[0]:
                        hit[1] = 1
                    if hit[1] != 0:
                        hit[0], hit[1], hit_done, dmg = Make_a_hit(hit[0], hit[1])
                else:
                    # Draw_weapon_packed(screen, lmb[0], x, y,charge)
                    Draw_Person(sprite_sheet, screen, scale, x + delta_camx, y+delta_camy, charge,Cx)
                    Draw_cursor(sprite_sheet, screen, scale, Cx+delta_camx, Cy+delta_camy)
                    Draw_weapon(sprite_sheet, screen, scale, x + delta_camx, y+delta_camy, Cx, Cy, hit[0],lmb[0],charge)
                # Camera_group().custom_draw(screen)


                x_dist, y_dist = round(int(Cx) - int(x)), round(-(int(Cy) - int(y)))
                camera_group.custom_draw(screen)

            except:pass
        print("yoooyy",Projectiles)
        Draw_inventory(screen)

        sock.send(str("!POS:" + str(pos) + "!MOUSE:" + str(cursor[0]) + " " + str(cursor[1]) + " " + "!KEYS:" + str(lmb) + "!INFOS:" + str(dmg)+" "+str(charge)+" "+str(Ready)+" "+str(k_e)+" ").encode())
        wasd = entities_onclient(Entities, screen, scale, sprite_sheet,delta_camx,delta_camy,x + delta_camx, y+delta_camy,k_e,wasd)
        if pause == True:
            Pause_menu(screen,cursor,lmb)
        print("pgr",Projectiles)
        draw_projectile(screen,Projectiles,delta_camx,delta_camy)

        Draw_cursor(sprite_sheet, screen, scale, cursor[0], cursor[1])
    pygame.display.flip()
