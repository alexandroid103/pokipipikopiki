Data = '300 300 walk 2 100 300 300 walk 2 100!ENT:zombie 700 300 2 0 0 False zombie 700 300 2 0 0 False!PROJ: 100 100 300 300 100 100 300 300 !ITEMS: 500 500 axe 500 500 axe'



def Decode_Data(Data):
        # This func actually decodes data that come from host and sort it as lists
        Players_data = Data[0:Data.find("!ENT:")]
        Entities_data = Data[Data.find("!ENT:"):Data.find("!PROJ:")].replace("!ENT:", "")
        Projectiles_data = Data[Data.find("!PROJ:"):Data.find("!ITEMS:")].replace("!PROJ:", "")
        Items_data = Data[Data.find("!ITEMS:"):Data.find("!QUEUE:")].replace("!QUEUE:", "")
        Queue_data = Data[Data.find("!QUEUE:"):Data.find("!NEXT:")].replace("!QUEUE:", "")
        Queue_data = Queue_data.split(" ")[0]
        Next_data = Data[Data.find("!NEXT:"):Data.find("!STAGE:")].replace("!NEXT:", "")
        Stage_data = Data[Data.find("!STAGE:"):len(Data)].replace("!STAGE:", "")
        Stage_data = Stage_data.split(" ")
        Stage_data = Stage_data[0]
        Players = []
        Players_data = Players_data.split(" ")
        for i in range(1,len(Players_data),7):
            try:
                Players.append([int(Players_data[i-1]),int(Players_data[i]),str(Players_data[i+1]),int(Players_data[i + 2]),int(Players_data[i + 3]),int(Players_data[i + 4]),int(Players_data[i + 5])])
            except:pass
        Entities = []
        Entities_data = Entities_data.split(" ")

        for i in range(0,len(Entities_data),10):
            try:
                Entities.append([str(Entities_data[i]),int(Entities_data[i+1]),int(Entities_data[i+2]),int(Entities_data[i + 3]),int(Entities_data[i + 4]),int(Entities_data[i + 5]),str(Entities_data[i + 6]),float(Entities_data[i + 7]),int(Entities_data[i + 8]),float(Entities_data[i + 9])])
            except:pass
        Projectiles = []

        Projectiles_data = Projectiles_data.split(" ")
        print(Projectiles_data[0])
        for i in range(0,len(Projectiles_data),7):
            try:
                print("amam",[float(Projectiles_data[i]),float(Projectiles_data[i+1]),int(Projectiles_data[i+2]),int(Projectiles_data[i+3]),int(Projectiles_data[i+4]),int(Projectiles_data[i+5]),str(Projectiles_data[i+6]),str(Projectiles_data[i+7])])
                Projectiles.append([float(Projectiles_data[i]),float(Projectiles_data[i+1]),int(Projectiles_data[i+2]),int(Projectiles_data[i+3]),int(Projectiles_data[i+4]),int(Projectiles_data[i+5]),str(Projectiles_data[i+6]),str(Projectiles_data[i+7])])
            except:pass
        print("gav",Projectiles)
        return Players,Entities,int(Queue_data),Next_data,Stage_data,Projectiles
def Client_decode(Data):
    # This func just decode and sort data that come to host from client.
    Pos_data = Data[Data.find("!POS:"):Data.find(" !MOUSE:")].replace("!POS:","")
    Pos_data = Pos_data.split(" ")

    # KEYS: лкм ...
    Cursor_data = Data[Data.find("!MOUSE:"):Data.find("!KEYS:")].replace("!MOUSE:","")
    Cursor_data = Cursor_data.split(" ")

    Keys_data = Data[Data.find("!KEYS:"):Data.find("!INFOS:")].replace("!KEYS:","")
    Keys_data = Keys_data.split(" ")

    Infos_data = [0,0]
    Infos_data = Data[Data.find("!INFOS:"):len(Data)].replace("!INFOS:","")
    print(Infos_data)
    Infos_data = Infos_data.split(" ")


    print("инфа",Infos_data[2])
    return Pos_data,Cursor_data,Keys_data,Infos_data[0],int(Infos_data[1]),Infos_data[2],Infos_data[3]
# Decode_Data(Data)
