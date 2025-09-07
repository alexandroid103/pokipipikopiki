import pygame
import time
import sys

clock = pygame.time.Clock()
pygame.init()
scale =4
sprite_sheet = pygame.transform.scale(pygame.image.load("new idea.png"),(pygame.image.load("new idea.png").get_width()*scale,pygame.image.load("new idea.png").get_height()*scale))
sprite_sheetx2 = pygame.transform.scale(pygame.image.load("new idea.png"),(pygame.image.load("new idea.png").get_width()*2,pygame.image.load("new idea.png").get_height()*2))
sprite_sheet_second = pygame.transform.scale(pygame.image.load("another idea.png"),(pygame.image.load("another idea.png").get_width()*scale,pygame.image.load("another idea.png").get_height()*scale))

# screen = pygame.display.set_mode((600,600))
def anim(screen,pos,spritesheet,areas,timer,secs,frames,last_update,flip):
    current_time = pygame.time.get_ticks()
    print(timer,secs)
    done = False
    try:
        sprite = spritesheet.subsurface((areas[int(timer)]))
        sprite = pygame.transform.flip(sprite,flip,0)
        screen.blit(sprite,pos)
    except:
        timer = 0
    if round(timer)>=len(areas)-1:
        timer = 0
        done = True
    else:
        print(current_time-last_update,secs/frames*1000)
        if current_time-last_update>=secs/frames:
            last_update = pygame.time.get_ticks()
            timer+=frames/secs/10

    return timer,last_update,done
shiny = {'timer':0,'last_update':0}
char = {'timer':0,'last_update':0}
trader = {'timer':0,'last_update':0}
item_column = {'timer':0,'last_update':0,'done':False}
living_armor = {'timer':0,'last_update':0}
wizzard = {'timer':0,'last_update':0}
gem = {'timer':0,'last_update':0}
ninja = {'timer':0,'last_update':0}
def ninja_attack_animation(screen,pos):
    ninja['timer'], ninja['last_update'], done = anim(screen, pos, sprite_sheet_second,
                                                      [(128 * 4, 0, 16 * 4, 16 * 4), (144 * 4, 0, 16 * 4, 16 * 4)
                                                          , (160 * 4, 0, 16 * 4, 16 * 4), (144 * 4, 0, 16 * 4, 16 * 4),
                                                       (128 * 4, 0, 16 * 4, 16 * 4)]
                                                      , ninja['timer'], 5, 6, ninja['last_update'], 0)
def ninja_run_animation(screen,pos):
    ninja['timer'],ninja['last_update'],done = anim(screen,pos,sprite_sheet_second,[(176*4,0,16*4,16*4),(192*4,0,16*4,16*4)
                                                                                    ,(208*4,0,16*4,16*4),(224*4,0,16*4,16*4),(240*4,0,16*4,16*4)]
                                                    ,ninja['timer'],5,6,ninja['last_update'],0)
def wizzard_run_animation(screen,pos):
    wizzard['timer'], wizzard['last_update'], done = anim(screen, pos, sprite_sheet_second,
                                                                    [(0 * 4, 230 * 4, 17 * 4, 20 * 4),
                                                                     (17 * 4, 230 * 4, 17 * 4, 20 * 4),
                                                                     (34 * 4, 230 * 4, 17 * 4, 20 * 4),
                                                                     (51 * 4, 230 * 4, 17 * 4, 20 * 4),
                                                                     (68 * 4, 230 * 4, 17 * 4, 20 * 4)
                                                                     ], wizzard['timer'], 5, 6,
                                                                    wizzard['last_update'],
                                                                    0)
def wizzard_attack_animation(screen,pos):
    wizzard['timer'], wizzard['last_update'], done = anim(screen, pos, sprite_sheet_second,
                                                          [(0 * 4, 255 * 4, 17 * 4, 20 * 4),
                                                           (17 * 4, 255 * 4, 17 * 4, 20 * 4),
                                                           (34 * 4, 255 * 4, 17 * 4, 20 * 4),
                                                           (51 * 4, 255 * 4, 17 * 4, 20 * 4),
                                                           (68 * 4, 255 * 4, 17 * 4, 20 * 4)
                                                           ], wizzard['timer'], 5, 6,
                                                          wizzard['last_update'],
                                                          0)
def living_armor_run_animation(screen,pos):
    living_armor['timer'], living_armor['last_update'], done = anim(screen, pos, sprite_sheet_second,
                                                                  [(0 * 4, 207 * 4, 17 * 4, 20 * 4),
                                                                   (17 * 4, 207 * 4, 17 * 4, 20 * 4),
                                                                   (34 * 4, 207 * 4, 17 * 4, 20 * 4),
                                                                   (51 * 4, 207 * 4, 17 * 4, 20 * 4),
                                                                   (68 * 4, 207 * 4, 17 * 4, 20 * 4)
                                                                   ], living_armor['timer'], 5, 6,
                                                                  living_armor['last_update'],

                                                                  0)
    return done
def living_armor_idle_animation(screen,pos):
    living_armor['timer'], living_armor['last_update'], done = anim(screen, pos, sprite_sheet_second,
                                                                  [(0 * 4, 163 * 4, 17 * 4, 20 * 4),
                                                                   (17 * 4, 163 * 4, 17 * 4, 20 * 4),
                                                                   (34 * 4, 163 * 4, 17 * 4, 20 * 4)
                                                                   ], living_armor['timer'], 3, 3,
                                                                  living_armor['last_update'],

                                                                  0)
def Item_column_animation(screen,pos):
    done = False

    if item_column['done'] == False:
        item_column['timer'], item_column['last_update'],done = anim(screen, pos, sprite_sheet_second,
                                                  [(0 * 4, 16*4, 16 * 4, 16 * 4), (16 * 4, 16*4, 16 * 4, 16 * 4),
                                                   (32 * 4, 16*4, 16 * 4, 16 * 4), (48 * 4, 16*4, 16 * 4, 16 * 4)
                                                   ], item_column['timer'], 20, 3, item_column['last_update'],

                                              0)
    else:
        screen.blit(sprite_sheet_second,pos,[0 * 4, 16*4, 16 * 4, 16 * 4])
    if done == True:
        item_column['done'] = True
def Trader_animation(screen,pos):
    global sprite_sheet_second,trader
    trader['timer'], trader['last_update'],done = anim(screen, pos, sprite_sheet_second,
                                              [(0 * 4, 0, 16 * 4, 16 * 4), (16 * 4, 0, 16 * 4, 16 * 4),
                                               (0 * 4, 0, 16 * 4, 16 * 4), (32 * 4, 0, 16 * 4, 16 * 4),(0 * 4, 0, 16 * 4, 16 * 4),(0 * 4, 0, 16 * 4, 16 * 4)
                                               ], trader['timer'], 20, 4, trader['last_update'],
                                              0)


def shine_animation(screen,pos):
    global sprite_sheetx2,char
    shiny['timer'],shiny['last_update'],done = anim(screen,pos,sprite_sheetx2,[(112*2,32*2,16*2,16*2),(128*2,32*2,16*2,16*2),(144*2,32*2,16*2,16*2),(160*2,32*2,16*2,16*2),(176*2,32*2,16*2,16*2),(112*2,48*2,16*2,16*2),(128*2,48*2,16*2,16*2)],shiny['timer'],5,6,shiny['last_update'],0)
def character_run_animation(screen,pos,lmb):
    global sprite_sheet, char
    if lmb>=pos[0]:
        char['timer'],char['last_update'],done = anim(screen,pos,sprite_sheet,[(32*4,0,16*4,16*4),(48*4,0,16*4,16*4),(64*4,0,16*4,16*4),(80*4,0,16*4,16*4),(96*4,0,16*4,16*4),(80*4,0,16*4,16*4),(64*4,0,16*4,16*4),(48*4,0,16*4,16*4),(32*4,0,16*4,16*4)],char['timer'],5,6,char['last_update'],0)
    else:
        char['timer'],char['last_update'],done = anim(screen,pos,sprite_sheet,[(32*4,0,16*4,16*4),(48*4,0,16*4,16*4),(64*4,0,16*4,16*4),(80*4,0,16*4,16*4),(96*4,0,16*4,16*4),(80*4,0,16*4,16*4),(64*4,0,16*4,16*4),(48*4,0,16*4,16*4),(32*4,0,16*4,16*4)],char['timer'],5,6,char['last_update'],1)

# timer,last_update
# (32*4,0,16*4,16*4),(48*4,0,16*4,16*4),(64*4,0,16*4,16*4),(80*4,0,16*4,16*4),(96*4,0,16*4,16*4),(80*4,0,16*4,16*4),(64*4,0,16*4,16*4),(48*4,0,16*4,16*4),(32*4,0,16*4,16*4)
# while True:
#     for event in pygame.event.get():
#         key_type = event.type
#         if event.type == pygame.QUIT:
#             sys.exit()
#             pygame.quit()
#
#     screen.blit(sprite_sheet, (0, 0), (32 * 4, 0, 16 * 4, 16 * 4))
#     screen.fill((100,100,100))
#     shine_animation(screen,(0,0))
#     character_run_animation(screen,(64,0))
#     time.sleep(0.01)
#     pygame.display.flip()
