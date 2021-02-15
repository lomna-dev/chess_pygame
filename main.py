import temp

import pygame
import pickle
import math
import Scripts.king as k
from Scripts.king import moveBlackKing,moveWhiteKing,checkThreats
from Scripts.pawn import movePawnWhite, movePawnBlack
from Scripts.rook import moveBlackRook, moveWhiteRook
from Scripts.knight import moveWhiteKnight,moveBlackKnight
from Scripts.bishop import moveWhiteBishop,moveBlackBishop
from Scripts.queen import moveBlackQueen,moveWhiteQueen

pygame.init()

checkBlack = False
checkWhite = False

widht = 500
height = 500
tob = False #short for turn of black
kingSurroundings = [[1,1],[0,1],[-1,1],[-1,0],[-1,-1],[0,-1],[1,-1],[1,0]]
win = pygame.display.set_mode((widht,height))

#Loading All The Required Images
boardImage = pygame.image.load("Assets/chess/board.png").convert()
wp = pygame.image.load("Assets/chess/whitepawn.png").convert_alpha()
bp = pygame.image.load("Assets/chess/blackpawn.png").convert_alpha()
wr = pygame.image.load("Assets/chess/whiterook.png").convert_alpha()
br = pygame.image.load("Assets/chess/blackrook.png").convert_alpha()
wkn = pygame.image.load("Assets/chess/whiteknight.png").convert_alpha()
bkn = pygame.image.load("Assets/chess/blackknight.png").convert_alpha()
wb = pygame.image.load("Assets/chess/whitebishop.png").convert_alpha()
bb = pygame.image.load("Assets/chess/blackbishop.png").convert_alpha()
wq = pygame.image.load("Assets/chess/whitequeen.png").convert_alpha()
bq = pygame.image.load("Assets/chess/blackqueen.png").convert_alpha()
wki = pygame.image.load("Assets/chess/whiteking.png").convert_alpha()
bki = pygame.image.load("Assets/chess/blackking.png").convert_alpha()
promoteImage = pygame.image.load("Assets/chess/promote.png").convert()
bluesquare = pygame.image.load("Assets/chess/bluesquare.png").convert_alpha()

#Draw The Board
#win.blit(pygame.transform.scale(boardImage, (height,height)),((widht-height)/2,0))

def changeTurn():
    z = pickle.load(open("turn.bin",'rb'))
    if z == True:
        pickle.dump(False,open("turn.bin",'wb'))
    else:
        pickle.dump(True,open("turn.bin",'wb'))

def findKings():
    z = pickle.load(open("data.bin",'rb'))
    whiteKing = []
    blackKing = []
    for y in range(8):
        for x in range(8):
            if z[x][y][0] == True and z[x][y][1] == 'b' and z[x][y][2] == 'ki':
                blackKing = [x,y]
            if z[x][y][0] == True and z[x][y][1] == 'w' and z[x][y][2] == 'ki':
                whiteKing = [x,y]
    return [whiteKing,blackKing]

#Function To Draw The Pieces
def DrawPieces():
    a = pickle.load(open("data.bin",'rb'))
    win.blit(pygame.transform.scale(boardImage, (height,height)),((widht-height)/2,0))
    for y in range(8):
        for x in range(8):
            if a[x][y][0] == True:
                if a[x][y][1] == 'w' and a[x][y][2]=='p': #Check for whitepawn
                    win.blit(pygame.transform.scale(wp,(math.floor(widht/8),math.floor(height/8))),[x*widht/8,y*height/8])
                if a[x][y][1] == 'b' and a[x][y][2]=='p': #Check for blackpawn
                    win.blit(pygame.transform.scale(bp,(math.floor(widht/8),math.floor(height/8))),[x*widht/8,y*height/8])
                if a[x][y][1] == 'w' and a[x][y][2] == 'r': #Check for white rook
                    win.blit(pygame.transform.scale(wr,(math.floor(widht/8),math.floor(height/8))), [x*widht/8,y*height/8])
                if a[x][y][1] == 'b' and a[x][y][2] == 'r': #Check for black rook
                    win.blit(pygame.transform.scale(br,(math.floor(widht/8),math.floor(height/8))), [x*widht/8,y*height/8])
                if a[x][y][1] == 'w' and a[x][y][2] == 'kn': #Check for white knight
                    win.blit(pygame.transform.scale(wkn,(math.floor(widht/8),math.floor(height/8))), [x*widht/8,y*height/8])
                if a[x][y][1] == 'b' and a[x][y][2] == 'kn': #Check for black knight
                    win.blit(pygame.transform.scale(bkn,(math.floor(widht/8),math.floor(height/8))), [x*widht/8,y*height/8])
                if a[x][y][1] == 'w' and a[x][y][2] == 'b': #Check for white bishop
                    win.blit(pygame.transform.scale(wb,(math.floor(widht/8),math.floor(height/8))), [x*widht/8,y*height/8])
                if a[x][y][1] == 'b' and a[x][y][2] == 'b': #Check for black bishop
                    win.blit(pygame.transform.scale(bb,(math.floor(widht/8),math.floor(height/8))), [x*widht/8,y*height/8])
                if a[x][y][1] == 'w' and a[x][y][2] == 'q': #Check for white queen
                    win.blit(pygame.transform.scale(wq,(math.floor(widht/8),math.floor(height/8))), [x*widht/8,y*height/8])
                if a[x][y][1] == 'b' and a[x][y][2] == 'q': #Check for black queen
                    win.blit(pygame.transform.scale(bq,(math.floor(widht/8),math.floor(height/8))), [x*widht/8,y*height/8])
                if a[x][y][1] == 'w' and a[x][y][2] == 'ki': #Check for white king
                    win.blit(pygame.transform.scale(wki,(math.floor(widht/8),math.floor(height/8))), [x*widht/8,y*height/8])
                if a[x][y][1] == 'b' and a[x][y][2] == 'ki': #Check for black king
                    win.blit(pygame.transform.scale(bki,(math.floor(widht/8),math.floor(height/8))), [x*widht/8,y*height/8])

def movement(clicka,clickb):
    global tob
    a = pickle.load(open("data.bin",'rb'))
    #Section for moving pieces
    if a[clicka[0]][clicka[1]][0] == True: #Check if a piece is selected and for check
        if tob == False and a[clicka[0]][clicka[1]][1] == 'w':         #check for white piece if turn is of white and if check on white
            if a[clicka[0]][clicka[1]][2] == 'p':   #Check if piece is a pawn
                movePawnWhite(clicka,clickb,promoteImage)  
            if a[clicka[0]][clicka[1]][2] == 'r':   #Check if piece is a rook
                if moveWhiteRook(clicka,clickb):
                    if clicka == [0,7]:
                        k.canCastle[2] = False
                    if clicka == [7,7]:
                        k.canCastle[3] = False  
            if a[clicka[0]][clicka[1]][2] == 'kn':   #Check if piece is a knight
                moveWhiteKnight(clicka,clickb) 
            if a[clicka[0]][clicka[1]][2] == 'b':   #Check if piece is a bishop
                moveWhiteBishop(clicka,clickb)
            if a[clicka[0]][clicka[1]][2] == 'q':   #Check if piece is a queen
                moveWhiteQueen(clicka,clickb)  
            if a[clicka[0]][clicka[1]][2] == 'ki':  #Check if piece is a king
                moveWhiteKing(clicka,clickb) 
        if tob == True and a[clicka[0]][clicka[1]][1] == 'b':          #Check for black piece if turn of black
            if a[clicka[0]][clicka[1]][2] == 'p':   #Check if piece is a pawn
                movePawnBlack(clicka,clickb,promoteImage)
            if a[clicka[0]][clicka[1]][2] == 'r':   #Check if piece is a rook
                if moveBlackRook(clicka,clickb):
                    if clicka == [0,0]:
                        k.canCastle[0] = False
                    if clicka == [7,0]:
                        k.canCastle[1] = False
            if a[clicka[0]][clicka[1]][2] == 'kn':   #Check if piece is a knight
                moveBlackKnight(clicka,clickb)
            if a[clicka[0]][clicka[1]][2] == 'b':   #Check if piece is a bishop
                moveBlackBishop(clicka,clickb)
            if a[clicka[0]][clicka[1]][2] == 'q':   #Check if piece is a queen
                moveBlackQueen(clicka,clickb)
            if a[clicka[0]][clicka[1]][2] == 'ki':  #Check if piece is a king
                moveBlackKing(clicka,clickb)
        if tob == True and a[clicka[0]][clicka[1]][1] == 'b':
            moveBlackKing(clicka,clickb)
        if tob == False and a[clicka[0]][clicka[1]][1] == 'w':
            moveWhiteKing(clicka,clickb)

#Gets The last two pair of click and makes reqired changes
def CheckClick(clicka,clickb):
    global checkWhite
    global checkBlack
    global tob
    a = pickle.load(open("data.bin",'rb'))
    #Section for looking for checks
    kings = findKings()
    whiteKing = kings[0]
    blackKing = kings[1]
    if checkThreats(whiteKing,whiteKing):
        checkWhite = True
        print("Check on white")
    if checkThreats(whiteKing,whiteKing) == False:
        checkWhite = False #No Check
    if checkThreats(blackKing,blackKing):
        checkBlack = True
        print("Check on black")
    if checkThreats(blackKing,blackKing) == False:
        checkBlack = False #No Check
        
    #Section for movement
    tob = pickle.load(open("turn.bin",'rb')) #Update the turn variable
    if tob == True and checkBlack == True:
        a = pickle.load(open("data.bin",'rb'))
        q = a
        movement(clicka,clickb)
        a = pickle.load(open("data.bin",'rb'))
        if q == a:
            pass
        else:
            ko = findKings()
            if checkThreats(ko[1],ko[1]):
                pickle.dump(q,open("data.bin",'wb'))
                DrawPieces()
                changeTurn()
            else:
                print("Evaded check")
    if tob == False and checkWhite == True:
        q = a
        movement(clicka,clickb)
        a = pickle.load(open("data.bin",'rb'))
        if q == a:
            pass
        else:
            kim = findKings()
            if checkThreats(kim[0],kim[0]):
                pickle.dump(q,open("data.bin",'wb'))
                changeTurn()
            else:
                print("Evaded check")
    if checkBlack == False and checkWhite == False:
        movement(clicka,clickb) #Handles the movement
    DrawPieces() #Draw after each move

#Draw The Board And Pieces Before Game Starts
DrawPieces()

local = [] #Store Two Clicks
#Main Loop Of the Game
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            #get the positon of mouse on chess board
            pos = [math.floor(pygame.mouse.get_pos()[0]/widht * 8),math.floor(pygame.mouse.get_pos()[1]/height * 8)]
            win.blit(pygame.transform.scale(bluesquare,(math.floor(widht/8),math.floor(height/8))),[pos[0]*widht/8,pos[1]*height/8])
            local.append(pos)
            if(len(local) >= 2):
                CheckClick(local[0],local[1])
                #print(local)
                local = []        
    #win.blit(pygame.transform.scale(boardImage, (height,height)),((widht-height)/2,0))
    pygame.display.update()