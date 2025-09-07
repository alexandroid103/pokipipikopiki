import pygame
import random
scale = 2
sprite_sheet = pygame.transform.scale(pygame.image.load("new idea.png"),(pygame.image.load("new idea.png").get_width()*scale,pygame.image.load("new idea.png").get_height()*scale))
# possible items you can get from chests
items = ["bloodstone","livingstone","bloodbite","poketmonster","prismatic","themurderer","soulpot","goldliver"]
# your current inventory
inventory = ["bloodstone","livingstone","bloodbite"]
# some kind of buffs u can get from items
# there are just a values of buffs you got from items the actual changes will be calculated soon in func
vampirism = 0 #%value
additional_hp = 0 #actual amount of health you got from items
damage_return = 0 #%value
damage_scale = 1 #damage multiplier for every attack
hp_regen = 0 #hp regeneration
# also there are some special fetures for some items that will be detected from this list:
buffs = []

def item_efficiency(hp,pos,dmg):
    global inventory,buffs,vampirism,additional_hp,damage_scale,damage_return
    vampirism = 0
    additional_hp = 0
    damage_return = 0
    damage_scale = 1
    for i in range(0,len(inventory)):
        name = inventory[i]
        if name == "bloodstone":
            additional_hp += 30
        if name == "prismatic":
            damage_return+=0.05
        if name == "themurderer":
            damage_scale+=0.1
        if name == "bloodbite":
            vampirism+=0.05
    print("вампиризм:",vampirism,"\дополнительное хп:",additional_hp,"\"возвращение уроона:",damage_return,"увеличение урона:",damage_scale)
    # return
def identify_item(name):
    global scale
    doll = [32 * scale, 32 * scale, 16 * scale, 16 * scale]
    if name == "bloodstone":
        doll = [32*scale,32*scale,16*scale,16*scale]
    elif name == "livingstone":
        doll = [32*scale,48*scale,16*scale,16*scale]
    elif name == "bloodbite":
        doll = [48*scale,48*scale,16*scale,16*scale]
    elif name == "poketmonster":
        doll = [32*scale,64*scale,16*scale,16*scale]
    elif name == "prismatic":
        doll = [48*scale,64*scale,16*scale,16*scale]
    elif name == "themurderer":
        doll = [32*scale,64*scale,16*scale,16*scale]
    elif name == "soulpot":
        doll = [80*scale,64*scale,16*scale,16*scale]
    elif name == "goldliver":
        doll = [80*scale,48*scale,16*scale,16*scale]
    return doll
def Draw_inventory(screen):
    global inventory,sprite_sheet,scale
    for i in range(0,len(inventory)):
        screen.blit(sprite_sheet,(10+i*(16*scale),20),identify_item(inventory[i]))

    pass
def Drop_random(value):
    global items
    chance = random.randint(0, len(items)-1)
    drop = items[chance]
    return drop





