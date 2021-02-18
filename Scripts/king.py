import pickle

a = pickle.load(open("data.bin",'rb'))

#Section to handle castling
canCastle = [True,True,
            True,True] #can castle for the four places we can in a game

def castle(posk,posr):
    q = pickle.load(open("data.bin",'rb'))
    if posr == [0,0] and canCastle[0]:
        print("Castle queen side for black side")
        k = 0
        s = 0
        for x in range(1,4):
            if q[x][0][0] == False:
                k += 1
        for x in range(2,5):
            if checkThreats(posk,[x,0])[0] == False:
                s += 1
        if k == 3 and s == 3:
            move(posk,[2, 0])
            move(posr, [3,0])
            changeTurn()
    if posr == [7,0] and canCastle[1]:
        print("Castle king side for black")
        k = 0
        s = 0
        for x in range(5,7):
            if q[x][0][0] == False:
                k += 1
        for x in range (4,7):
            if checkThreats(posk, [x,0])[0] == False:
                s += 1
        if k == 2 and s == 3:
            move(posk,[6,0])
            move(posr, [5,0])
            changeTurn()
    if posr == [0,7] and canCastle[2]:
        print("Castle queen side for white")
        k = 0
        s = 0
        for x in range(1,4):
            if q[x][7][0] == False:
                k += 1
        for x in range(2,5):
            if checkThreats(posk,[x,7])[0] == False:
                s += 1
        if k == 3 and s == 3:
            move(posk,[2, 7])
            move(posr, [3,7])
            changeTurn()
    if posr == [7,7] and canCastle[3]:
        print("Castle king side for white")
        k = 0
        s = 0
        for x in range(5,7):
            if q[x][7][0] == False:
                k += 1
        for x in range (4,7):
            if checkThreats(posk, [x,7])[0] == False:
                s += 1
        if k == 2 and s == 3:
            move(posk,[6,7])
            move(posr, [5,7])
            changeTurn()
    
#Section to handle movement
def move(posa,posb):
    z=pickle.load(open("data.bin",'rb'))
    if z[posa[0]][posa[1]][2] == 'r' or z[posa[0]][posa[1]][2] == 'ki':
        if (z[posa[0]][posa[1]][2] == 'r' and [abs(posb[0] - posa[0]),abs(posb[1] - posa[1])] != [1,1]) or z[posa[0]][posa[1]][2] == 'ki':
            colour = z[posa[0]][posa[1]][1]
            piece = z[posa[0]][posa[1]][2]
            z[posa[0]][posa[1]][0] = False
            z[posb[0]][posb[1]][1] = colour
            z[posb[0]][posb[1]][2] = piece
            z[posb[0]][posb[1]][0] = True
            pickle.dump(z,open("data.bin",'wb'))
            changeTurn()
            import Scripts.pawn as p
            p.enpassant[0] = False

knightThreats = [[1,-2],[2,-1],[2,1],[1,2],[-1,2],[-2,1],[-2,-1],[-1,-2]]

def changeTurn():
    z = pickle.load(open("turn.bin",'rb'))
    if z == True:
        pickle.dump(False,open("turn.bin",'wb'))
    else:
        pickle.dump(True,open("turn.bin",'wb'))

def moveBlackKing(posa,posb):
    if checkThreats(posa,posb)[0]:
        pass
    else:
        z = pickle.load(open("data.bin",'rb'))
        x = posb[0]-posa[0]
        y = posb[1]-posa[1]
        t = [abs(x),abs(y)]
        if posa == posb:
            pass
        elif t == [1,1] or t == [1,0] or t == [0,1]:
            if z[posb[0]][posb[1]][0] == False or z[posb[0]][posb[1]][1] == 'w':
                move(posa,posb)
                if posb != [0,0] or posb != [7,0]:
                    canCastle[0] = False
                    canCastle[1] = False
        elif posa == [4,0] and (posb == [0,0] or posb == [7,0]) and z[posb[0]][posb[1]][0] == True and z[posb[0]][posb[1]][2] == 'r':
            castle(posa,posb)

def moveWhiteKing(posa,posb):
    if checkThreats(posa,posb)[0]:
        pass
    else:
        z = pickle.load(open("data.bin",'rb'))
        x = posb[0]-posa[0]
        y = posb[1]-posa[1]
        t = [abs(x),abs(y)]
        if posa == posb:
            pass
        elif t == [1,1] or t == [1,0] or t == [0,1]:
            if z[posb[0]][posb[1]][0] == False or z[posb[0]][posb[1]][1] == 'b':
                move(posa,posb)
                if posb != [0,7] or posb != [7,7]:
                    canCastle[2] = False
                    canCastle[3] = False
        elif posa == [4,7] and (posb == [0,7] or posb == [7,7]) and z[posb[0]][posb[1]][0] == True and z[posb[0]][posb[1]][2] == 'r':
            castle(posa,posb)

def checkThreats(posa,posb):
    z = pickle.load(open("data.bin",'rb'))
    colourOfKing = z[posa[0]][posa[1]][1]
    colourOfOpponent = ''
    if colourOfKing == 'w':
        colourOfOpponent = 'b'
    else:
        colourOfOpponent = 'w'
    for i in range(1,8):    #Check in first quadrant
        currentBlock = [posb[0]+i,posb[1]-i]
        if posb[0] + i == 8 or posb[1] - i == -1:
            break
        if z[currentBlock[0]][currentBlock[1]][0] == True and z[currentBlock[0]][currentBlock[1]][1] == colourOfKing:
            break
        if i == 1 and colourOfKing == 'w' and z[currentBlock[0]][currentBlock[1]][0] == True and z[currentBlock[0]][currentBlock[1]][1] == 'b' and z[currentBlock[0]][currentBlock[1]][2] == 'p': #pawn threat
            #print("Black Pawn threat")
            return [True,currentBlock]
        if i == 1 and z[currentBlock[0]][currentBlock[1]][0] == True and z[currentBlock[0]][currentBlock[1]][1] == colourOfOpponent and z[currentBlock[0]][currentBlock[1]][2] == 'k': #King thrreat
            #print("King threat")
            return [True,currentBlock]
        if z[currentBlock[0]][currentBlock[1]][0] == True and z[currentBlock[0]][currentBlock[1]][1] == colourOfOpponent and (z[currentBlock[0]][currentBlock[1]][2] != 'b' and z[currentBlock[0]][currentBlock[1]][2] != 'q'):
            break
        if z[currentBlock[0]][currentBlock[1]][0] == True and z[currentBlock[0]][currentBlock[1]][1] == colourOfOpponent and (z[currentBlock[0]][currentBlock[1]][2] == 'b' or z[currentBlock[0]][currentBlock[1]][2] == 'q'): #queen of bishop threat
            #print("bishop or queen threat")
            return [True,currentBlock]
    for i in range(1,8):    #Check in second quadrant
        currentBlock = [posb[0]-i,posb[1]-i]
        if posb[0] - i == -1 or posb[1] - i == -1:
            break
        if z[currentBlock[0]][currentBlock[1]][0] == True and z[currentBlock[0]][currentBlock[1]][1] == colourOfKing:
            break
        if i == 1 and colourOfKing == 'w' and z[currentBlock[0]][currentBlock[1]][0] == True and z[currentBlock[0]][currentBlock[1]][1] == 'b' and z[currentBlock[0]][currentBlock[1]][2] == 'p': #pawn threat
            #print("Black Pawn threat")
            return [True,currentBlock]
        if i == 1 and z[currentBlock[0]][currentBlock[1]][0] == True and z[currentBlock[0]][currentBlock[1]][1] == colourOfOpponent and z[currentBlock[0]][currentBlock[1]][2] == 'k': #King thrreat
            #print("King threat")
            return [True,currentBlock]
        if z[currentBlock[0]][currentBlock[1]][0] == True and z[currentBlock[0]][currentBlock[1]][1] == colourOfOpponent and (z[currentBlock[0]][currentBlock[1]][2] != 'b' and z[currentBlock[0]][currentBlock[1]][2] != 'q'):
            break
        if z[currentBlock[0]][currentBlock[1]][0] == True and z[currentBlock[0]][currentBlock[1]][1] == colourOfOpponent and (z[currentBlock[0]][currentBlock[1]][2] == 'b' or z[currentBlock[0]][currentBlock[1]][2] == 'q'): #queen of bishop threat
            #print("bishop or queen threat")
            return [True,currentBlock]
    for i in range(1,8):    #Check in third quadrant
        currentBlock = [posb[0]-i,posb[1]+i]
        if posb[0] - i == -1 or posb[1] + i == 8:
            break
        if z[currentBlock[0]][currentBlock[1]][0] == True and z[currentBlock[0]][currentBlock[1]][1] == colourOfKing:
            break
        if i == 1 and colourOfKing == 'b' and z[currentBlock[0]][currentBlock[1]][0] == True and z[currentBlock[0]][currentBlock[1]][1] == 'w' and z[currentBlock[0]][currentBlock[1]][2] == 'p': #pawn threat
            #print("White Pawn threat")
            return [True,currentBlock]
        if i == 1 and z[currentBlock[0]][currentBlock[1]][0] == True and z[currentBlock[0]][currentBlock[1]][1] == colourOfOpponent and z[currentBlock[0]][currentBlock[1]][2] == 'k': #King thrreat
            #print("King threat")
            return [True,currentBlock]
        if z[currentBlock[0]][currentBlock[1]][0] == True and z[currentBlock[0]][currentBlock[1]][1] == colourOfOpponent and (z[currentBlock[0]][currentBlock[1]][2] != 'b' and z[currentBlock[0]][currentBlock[1]][2] != 'q'):
            break
        if z[currentBlock[0]][currentBlock[1]][0] == True and z[currentBlock[0]][currentBlock[1]][1] == colourOfOpponent and (z[currentBlock[0]][currentBlock[1]][2] == 'b' or z[currentBlock[0]][currentBlock[1]][2] == 'q'): #queen of bishop threat
            #print("bishop or queen threat")
            return [True,currentBlock]
    for i in range(1,8):    #Check in fourth quadrant
        currentBlock = [posb[0]+i,posb[1]+i]
        if posb[0] + i == 8 or posb[1] + i == 8:
            break
        if z[currentBlock[0]][currentBlock[1]][0] == True and z[currentBlock[0]][currentBlock[1]][1] == colourOfKing:
            break
        if i == 1 and colourOfKing == 'b' and z[currentBlock[0]][currentBlock[1]][0] == True and z[currentBlock[0]][currentBlock[1]][1] == 'w' and z[currentBlock[0]][currentBlock[1]][2] == 'p': #pawn threat
            #print("White Pawn threat")
            return [True,currentBlock]
        if i == 1 and z[currentBlock[0]][currentBlock[1]][0] == True and z[currentBlock[0]][currentBlock[1]][1] == colourOfOpponent and z[currentBlock[0]][currentBlock[1]][2] == 'k': #King thrreat
            #print("King threat")
            return [True,currentBlock]
        if z[currentBlock[0]][currentBlock[1]][0] == True and z[currentBlock[0]][currentBlock[1]][1] == colourOfOpponent and (z[currentBlock[0]][currentBlock[1]][2] != 'b' and z[currentBlock[0]][currentBlock[1]][2] != 'q'):
            break
        if z[currentBlock[0]][currentBlock[1]][0] == True and z[currentBlock[0]][currentBlock[1]][1] == colourOfOpponent and (z[currentBlock[0]][currentBlock[1]][2] == 'b' or z[currentBlock[0]][currentBlock[1]][2] == 'q'): #queen of bishop threat
            #print("bishop or queen threat")
            return [True,currentBlock]
    for i in range(1,8):    #Check in +ve x axis
        currentBlock = [posb[0]+i,posb[1]]
        if currentBlock[0] == 8:
            break
        if z[currentBlock[0]][currentBlock[1]][0] == True and z[currentBlock[0]][currentBlock[1]][1] == colourOfKing:
            break
        if z[currentBlock[0]][currentBlock[1]][0] == True and z[currentBlock[0]][currentBlock[1]][1] == colourOfOpponent and (z[currentBlock[0]][currentBlock[1]][2] != 'r' and z[currentBlock[0]][currentBlock[1]][2] != 'q'):
            break
        if z[currentBlock[0]][currentBlock[1]][0] == True and z[currentBlock[0]][currentBlock[1]][1] == colourOfOpponent and (z[currentBlock[0]][currentBlock[1]][2] == 'r' or z[currentBlock[0]][currentBlock[1]][2] == 'q'): #Rook or queen threat
            #print("Rook or queen threat along +ve x")
            return [True,currentBlock]
    for i in range(1,8):    #Check in -ve x axis
        currentBlock = [posb[0]-i,posb[1]]
        if currentBlock[0] == -1:
            break
        if z[currentBlock[0]][currentBlock[1]][0] == True and z[currentBlock[0]][currentBlock[1]][1] == colourOfKing:
            break
        if z[currentBlock[0]][currentBlock[1]][0] == True and z[currentBlock[0]][currentBlock[1]][1] == colourOfOpponent and (z[currentBlock[0]][currentBlock[1]][2] != 'r' and z[currentBlock[0]][currentBlock[1]][2] != 'q'):
            break
        if z[currentBlock[0]][currentBlock[1]][0] == True and z[currentBlock[0]][currentBlock[1]][1] == colourOfOpponent and (z[currentBlock[0]][currentBlock[1]][2] == 'r' or z[currentBlock[0]][currentBlock[1]][2] == 'q'): #Rook or queen threat
            #print("Rook or queen threat along -ve x")
            return [True,currentBlock]
    for i in range(1,8):    #Check in +ve y axis
        currentBlock = [posb[0],posb[1]+i]
        if currentBlock[1] == 8:
            break
        if z[currentBlock[0]][currentBlock[1]][0] == True and z[currentBlock[0]][currentBlock[1]][1] == colourOfKing:
            break
        if z[currentBlock[0]][currentBlock[1]][0] == True and z[currentBlock[0]][currentBlock[1]][1] == colourOfOpponent and (z[currentBlock[0]][currentBlock[1]][2] != 'r' and z[currentBlock[0]][currentBlock[1]][2] != 'q'):
            break
        if z[currentBlock[0]][currentBlock[1]][0] == True and z[currentBlock[0]][currentBlock[1]][1] == colourOfOpponent and (z[currentBlock[0]][currentBlock[1]][2] == 'r' or z[currentBlock[0]][currentBlock[1]][2] == 'q'): #Rook or queen threat
            #print("Rook or queen threat along +ve y axis")
            return [True,currentBlock]
    for i in range(1,8):    #Check in -ve y axis
        currentBlock = [posb[0],posb[1]-i]
        if currentBlock[1] == -1:
            break
        if z[currentBlock[0]][currentBlock[1]][0] == True and z[currentBlock[0]][currentBlock[1]][1] == colourOfKing:
            break
        if z[currentBlock[0]][currentBlock[1]][0] == True and z[currentBlock[0]][currentBlock[1]][1] == colourOfOpponent and (z[currentBlock[0]][currentBlock[1]][2] != 'r' and z[currentBlock[0]][currentBlock[1]][2] != 'q'):
            break 
        if z[currentBlock[0]][currentBlock[1]][0] == True and z[currentBlock[0]][currentBlock[1]][1] == colourOfOpponent and (z[currentBlock[0]][currentBlock[1]][2] == 'r' or z[currentBlock[0]][currentBlock[1]][2] == 'q'): #Rook or queen threat
            #print("Rook or queen threat along -ve y")
            return [True,currentBlock]
    for t in knightThreats:
        p = [posb[0] + t[0],posb[1] + t[1]]
        if p[0] > 7 or p[0] < 0 or p[1] > 7 or p[1] < 0:
            continue
        else:
            if z[p[0]][p[1]][0] == True and z[p[0]][p[1]][1] == colourOfOpponent and z[p[0]][p[1]][2] == 'kn':
                #print("knight threat")
                return [True,p]
    return [False,[-1,-4]]