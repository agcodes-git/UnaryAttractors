import pygame
import key_input as IN
import copy
import convert
import math
import sys


pygame.init()
width = 400
height = 400
s = pygame.display.set_mode((width,height))
p_clock = pygame.time.Clock()

rule = 0
base = 3

while True:

    IN.last_keys_down = copy.deepcopy(IN.keys_down)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        elif event.type == pygame.KEYDOWN: IN.keys_down[str(event.key)] = True
        elif event.type == pygame.KEYUP: IN.keys_down[str(event.key)] = False
        elif event.type == pygame.MOUSEBUTTONUP: IN.keys_down[str(event.button)] = False
        elif event.type == pygame.MOUSEBUTTONDOWN: IN.keys_down[str(event.button)] = True
        elif event.type == pygame.MOUSEMOTION: IN.mouse_position = event.pos

    pygame.draw.rect(s,(20,20,20),(0,0,width,height))

    if IN.down(pygame.K_UP) and rule < base**base-1: rule += 1
    elif IN.down(pygame.K_DOWN) and rule > 0: rule -= 1

    if IN.down(pygame.K_UP) and IN.down(pygame.K_s) and rule+int(math.sqrt(base**base)) < base**base: rule += int(math.sqrt(base**base))
    elif IN.down(pygame.K_DOWN) and IN.down(pygame.K_s) and rule-int(math.sqrt(base**base)) > 0: rule -= int(math.sqrt(base**base))

    if IN.pressed(pygame.K_RIGHT) and base < 10:
        base += 1
        rule = 0
    elif IN.pressed(pygame.K_LEFT) and base > 1:
        base -= 1
        rule = 0

    graphs = [[] for k in range(base)]
    r = convert.n2s(rule % (base**base),base,base)
    for x in range(base):
        for compose in range(base):
            graphs[compose].append(x)
            x = int(r[x])

    if IN.pressed(pygame.K_SPACE):
        print( graphs )

    if IN.pressed(pygame.K_m):
        rule = int((base**base)/2)

    scale = 350/(base+2)
    for g in range(len(graphs)):
        for e in range(len(graphs[g])):
            m = 255 / (len(graphs[g])+3)
            color = (255,0,0) if g == 0 else (0,m*(g+3),0)
            if e > 0:
                pygame.draw.line(s,color,(e*scale+width/10,-graphs[g][e]*scale+height-50),((e-1)*scale+width/10,-graphs[g][e-1]*scale+height-50))
            pygame.draw.rect(s,color,(e*scale + width/10,-graphs[g][e]*scale + height-50 ,1,1))
            if graphs[g][e] == e and g > 0:
                pygame.draw.ellipse(s,(255,0,255),(e*scale+width/10-scale/2,-graphs[g][e]*scale+height-50-scale/2,scale,scale),1)

    basicfont = pygame.font.SysFont(None,24)
    text = basicfont.render('Rule: '+str(rule),True, (90,90,90))
    s.blit(text, (50,height-20,100,20))

    basicfont = pygame.font.SysFont(None,24)
    text = basicfont.render('Base: '+str(base),True, (90,90,90))
    s.blit(text, (width-100,height-20,100,20))

    pygame.display.flip()
    p_clock.tick(60)