import pygame
import pickle
pygame.init()

def changeTurn():
    z = pickle.load(open("turn.bin",'rb'))
    if z == True:
        pickle.dump(False,open("turn.bin",'wb'))
    else:
        pickle.dump(True,open("turn.bin",'wb'))
    
def remove(pos):
    m = pickle.load(open("data.bin",'rb'))
    m[pos[0]][pos[1]][0] = False
    pickle.dump(m,open("data.bin",'wb'))

def Promote(posa,posb,m,img):
    win = pygame.display.set_mode(pygame.display.get_window_size())
    win.blit(pygame.transform.scale(img,pygame.display.get_window_size()),(0,0))
    pygame.display.update()
    running = True
    while running:
        for  event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    print("Queen")
                    m[posb[0]][posb[1]][2] = 'q'
                    running = False
                    return m
                if event.key == pygame.K_RIGHT:
                    print("Bishop")
                    m[posb[0]][posb[1]][2] = 'b'
                    running = False
                    return m
                if event.key == pygame.K_UP:
                    print("Rook")
                    m[posb[0]][posb[1]][2] = 'r'
                    running = False
                    return m
                if event.key == pygame.K_DOWN:
                    print("Knight")
                    m[posb[0]][posb[1]][2] = 'kn'
                    running = False
                    return m

enpassant = [False,[8,8]]
#makes changes to main data file
def movePawnWhite(posa,posb,img):
    global enpassant
    a = pickle.load(open("data.bin",'rb'))
    if [posa[0] - 1,posa[1] - 1] == posb and a[posb[0]][posb[1]][0] == True and a[posb[0]][posb[1]][1] == 'b':
        MoveWhite(posa,posb,img)
        enpassant[0] = False
    if [posa[0] + 1,posa[1] - 1] == posb and a[posb[0]][posb[1]][0] == True and a[posb[0]][posb[1]][1] == 'b':
        MoveWhite(posa,posb,img)
        enpassant[0] = False
    if [posa[0],posa[1] - 1] == posb and a[posa[0]][posa[1]-1][0] == False:
        MoveWhite(posa,posb,img)
        enpassant[0] = False
    if [posa[0],posa[1]-2] == posb and a[posa[0]][posa[1]-1][0] == False and posa[1] == 6:
        MoveWhite(posa,posb,img)
        if posa[0] > 0 and posa[0] < 7:
            if a[posb[0]+1][posb[1]][0] == True and a[posb[0]+1][posb[1]][1] == 'b' and a[posb[0]+1][posb[1]][2] == 'p':
                enpassant = [True,[posb[0],posb[1]+1]]
            elif a[posb[0]-1][posb[1]][0] == True and a[posb[0]-1][posb[1]][1] == 'b' and a[posb[0]-1][posb[1]][2] == 'p':
                enpassant = [True,[posb[0],posb[1]+1]]
            else:
                enpassant[0] = False
        if posa[0] == 0:
            if a[posb[0]+1][posb[1]][0] == True and a[posb[0]+1][posb[1]][1] == 'b' and a[posb[0]+1][posb[1]][2] == 'p':
                enpassant = [True,[posb[0],posb[1]+1]]
            else:
                enpassant[0] = False
        if posa[0] == 7:
            if a[posb[0]-1][posb[1]][0] == True and a[posb[0]-1][posb[1]][1] == 'b' and a[posb[0]-1][posb[1]][2] == 'p':
                enpassant = [True,[posb[0],posb[1]+1]]
            else:
                enpassant[0] = False
    if posb == enpassant[1] and a[enpassant[1][0]][enpassant[1][1]][0] == False and enpassant[0] == True:
        MoveWhite(posa,posb,img)
        remove([posb[0],posb[1]+1])


def movePawnBlack(posa,posb,img):
    global enpassant
    a = pickle.load(open("data.bin",'rb'))
    if [posa[0] - 1,posa[1] + 1] == posb and a[posb[0]][posb[1]][0] == True and a[posb[0]][posb[1]][1] == 'w':
        MoveBlack(posa,posb,img)
        enpassant[0] = False
    if [posa[0] + 1,posa[1] + 1] == posb and a[posb[0]][posb[1]][0] == True and a[posb[0]][posb[1]][1] == 'w':
        MoveBlack(posa,posb,img)
        enpassant[0] = False
    if [posa[0],posa[1] + 1] == posb and a[posb[0]][posb[1]][0] == False:
        MoveBlack(posa,posb,img)
        enpassant[0] = False
    if [posa[0],posa[1]+2] == posb and a[posa[0]][posa[1]+1][0] == False and posa[1] == 1:
        MoveBlack(posa,posb,img)
        if posa[0] > 0 and posa[0] < 7:
            if a[posb[0]+1][posb[1]][0] == True and a[posb[0]+1][posb[1]][1] == 'w' and a[posb[0]+1][posb[1]][2] == 'p':
                enpassant = [True,[posb[0],posb[1]-1]]
            elif a[posb[0]-1][posb[1]][0] == True and a[posb[0]-1][posb[1]][1] == 'w' and a[posb[0]-1][posb[1]][2] == 'p':
                enpassant = [True,[posb[0],posb[1]-1]]
            else:
                enpassant[0] = False
        if posa[0] == 0:
            if a[posb[0]+1][posb[1]][0] == True and a[posb[0]+1][posb[1]][1] == 'w' and a[posb[0]+1][posb[1]][2] == 'p':
                enpassant = [True,[posb[0],posb[1]-1]]
            else:
                enpassant[0] = False
        if posa[0] == 7:
            if a[posb[0]-1][posb[1]][0] == True and a[posb[0]-1][posb[1]][1] == 'w' and a[posb[0]-1][posb[1]][2] == 'p':
                enpassant = [True,[posb[0],posb[1]-1]]
            else:
                enpassant[0] = False
    if posb == enpassant[1] and a[enpassant[1][0]][enpassant[1][1]][0] == False and enpassant[0] == True:
        MoveBlack(posa,posb,img) 
        remove([posb[0],posb[1]-1])

    
def MoveBlack(posa,posb,img):
    z = pickle.load(open("data.bin",'rb'))
    z[posa[0]][posa[1]][0] = False
    z[posb[0]][posb[1]][0] = True
    z[posb[0]][posb[1]][1] = 'b'
    z[posb[0]][posb[1]][2] = 'p'
    if posb[1] == 7:
        z = Promote(posa,posb,z,img)
    pickle.dump(z,open("data.bin",'wb'))
    changeTurn()

def MoveWhite(posa,posb,img):
    z = pickle.load(open("data.bin",'rb'))
    z[posa[0]][posa[1]][0] = False
    z[posb[0]][posb[1]][0] = True
    z[posb[0]][posb[1]][1] = 'w'
    z[posb[0]][posb[1]][2] = 'p'
    if posb[1] == 0:
        z= Promote(posa,posb,z,img)
    pickle.dump(z,open("data.bin",'wb'))
    changeTurn()