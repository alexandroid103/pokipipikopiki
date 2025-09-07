import socket
import time
from test import Client_decode
from Try_a_level import fill_entities,entities_itself,Loot_chest
from Player import projectile
import pygame.time
import random
from Items import identify_item,Drop_random
clock = pygame.time.Clock()
FPS = 100

main_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
main_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Переиспользование адреса
main_socket.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
main_socket.setsockopt(socket.IPPROTO_TCP,socket.TCP_NODELAY,1)
main_socket.bind(('26.247.173.52',10000))

main_socket.setblocking(0)
main_socket.listen(5)
# listening to people who want to join
# 5 - how many people can play together
players_sockets = []
positions = []
entities = []
projecyiles = []
fill_entities(1,entities)
projectiles = [[0,0,0,0,2000,2000,"fireball"]]
stage = 0
Next = False
k_e = False
Pos_data = [0,0]
while True:
    # проверим есть ли желающие
    try:
        new_socket,addres = main_socket.accept()
        # returns users socket and their ip
        print('Подключился', addres,new_socket)

        new_socket.setblocking(0)
        players_sockets.append(new_socket)
        new_socket.send(str(players_sockets.index(new_socket)).encode())
        positions.append([ 300,300,'walk',2,100,0,0 ])
    except:
        # print('Нет желающих')
        pass

    # setblocking not to delay while True
    # считываем команды игроков
    # print(positions)
    x,y = 0,0
    Cx,Cy =0,0
    Next = True
    k_e = True
    for sock in players_sockets:
        data = '0 0'
        try:
            data = sock.recv(1024)
            data = data.decode()

            # print("~игрок~"+str(players_sockets.index(sock)))
            # print(data.split()[0])
            # print(data.split()[0])
            # print('Получил',data.split()[0],data.split()[1],players_sockets.index(sock))
            Pos_data, Cursor_data,Keys_data,Infos,Damage,Rdy,k_e = Client_decode(data)
            positions[players_sockets.index(sock)][0]+=int(Pos_data[0])
            positions[players_sockets.index(sock)][1] += int(Pos_data[1])
            positions[players_sockets.index(sock)][5],positions[players_sockets.index(sock)][6] = Cursor_data[0],Cursor_data[1]

            x,y = positions[players_sockets.index(sock)][0],positions[players_sockets.index(sock)][1]
            Cx,Cy = positions[players_sockets.index(sock)][5],positions[players_sockets.index(sock)][6]

            x_dist,y_dist =round(int(Cx) - int(x)),round(-(int(Cy) - int(y)))
            print(int(Pos_data[0]),int(Pos_data[1]))
            attack_area = round(x + (100 / (y_dist ** 2 + x_dist ** 2) ** 0.5) * x_dist), round(
                y - (100 / (y_dist ** 2 + x_dist ** 2) ** 0.5) * y_dist)
            if str(Rdy) == "False":
                Next = False

            for i in range(0,len(entities)):
                if entities[i][9]>0:
                    if entities[i][1] in range(attack_area[0]-100,attack_area[0]+100) and entities[i][2] in range(attack_area[1]-100,attack_area[1]+100) and Infos == "True":
                        entities[i][9]-=int(Damage)
                        if entities[i][9]<=0:
                            ch = random.randint(0,10)
                            if ch in range(0,2):
                                entities.remove(entities[i])
                            else:
                                entities[i][0] = "closed"


                else:
                    if entities[i][0] == "closed":
                        entities[i][6] = Drop_random(1)
                    entities[i][0] = Loot_chest(entities[i][1],entities[i][2],x,y,entities[i][0],k_e,entities[i][6])


        except:Next = False
    # данные от клиента, приходят в байтах их нужно расшифровать
    # обрабатываем команды
    # отрисовываем новое поле
    try:
        data_poses = ""
        data_projectiles = ""
        for i in range(0,len(projectiles)):
            projectile("",projectiles,0,0)
            data_projectiles = data_projectiles + str(projectiles[i][0]) + " " + str(projectiles[i][1]) + " " + str(projectiles[i][2]) + " " + str(projectiles[i][3]) + " " + str(projectiles[i][4]) + " " + str(projectiles[i][5]) + " " + str(projectiles[i][6])+" "

        for i in range(0,len(positions)):
            data_poses = data_poses+str(str(positions[i][0]))+" "+str(positions[i][1])+" "+str(positions[i][2])+" "+str(positions[i][3])+" "+str(positions[i][4])+" "+str(positions[i][5])+" "+str(positions[i][6])+" "

        data_entities = []
        for i in range(0,len(entities)):

            data_entities.append(str(entities[i][0])+" "+str(entities[i][1])+" "+str(entities[i][2])+" "+str(entities[i][3])+" "+str(entities[i][4])+" "+str(entities[i][5])+" "+str(entities[i][6])+" "+str(entities[i][7])+" "+str(entities[i][8])+" "+str(entities[i][9]))

        # print(data_poses)
        data_entities = str(data_entities).replace('[',"")
        data_entities = data_entities.replace(']','')
        data_entities = data_entities.replace("'", "")
        data_entities = data_entities.replace(",", "")

    except:pass
    done = True
    for i in range(0,len(entities)):

        if entities[i][9]>0:
            done = False
    if Next == True and done == True:
        stage += 1
        entities.clear()
        fill_entities(stage+1, entities)
    for sock in players_sockets:
        try:
            pos = str(str(positions[players_sockets.index(sock)][0])+" "+str(positions[players_sockets.index(sock)][1])+" ")
            # print((str(data_poses)+"!ENT:"+data_entities+str(players_sockets.index(sock))+"!PROJ:"+"!ITEMS"))
            # sock.send((str(data_poses)+"&"+data_entities+str(players_sockets.index(sock))).encode())
            # sock.send("попка".encode())
            sock.sendall(str(str(data_poses)+"!ENT:"+str(data_entities)+"!PROJ:"+str(data_projectiles)+"!ITEMS:"+" "+"!QUEUE:"+str(players_sockets.index(sock))+"!NEXT:"+str(Next)+"!STAGE:"+str(stage)+" ").encode())
            # sock.send(str(len((str(data_poses)+"&"+data_entities+str(players_sockets.index(sock)))).encode()))
            # sock.send(data_entities.encode())
            # print(data_poses)

            for i in range(0, len(entities)):
                step = [0,0]
                print(Pos_data,"koma")
                step[0],step[1],best,entities[i][6],entities[i][7],entities[i][8],projectiles,entities[i][9]= entities_itself(entities, positions[players_sockets.index(sock)][0],
                                positions[players_sockets.index(sock)][1],i,k_e,projectiles,(int(Pos_data[0]),int(Pos_data[1])))

                entities[i][1]+=step[0]
                entities[i][2]+=step[1]

        except:
            positions.remove(positions[players_sockets.index(sock)])
            players_sockets.remove(sock)

            sock.close()
            print('Отключился игрок.')
            pass

    time.sleep(0.01)
    # clock.tick(FPS)