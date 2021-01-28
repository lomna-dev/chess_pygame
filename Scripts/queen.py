import pickle

def changeTurn():
    z = pickle.load(open("turn.bin",'rb'))
    if z == True:
        pickle.dump(False,open("turn.bin",'wb'))
    else:
        pickle.dump(True,open("turn.bin",'wb'))

def moveWhiteQueen(posa,posb):
    z = pickle.load(open( "data.bin",'rb'))
    if posa == posb: #Chechk if position a and b are same
        pass
    else:
        if (posb[0] - posa[0]) > 0 and posa[1] == posb[1]: #Towards +ve x
            for i in range(1,posb[0]-posa[0]+1):
                if z[posa[0] + i][posa[1]][0] == True and (z[posa[0] + i][posa[1]][1] == 'w' or (z[posa[0] + i][posa[1]][1] == 'b' and [posa[0]+i,posa[1]] != posb)):
                    break
                if [posa[0] + i,posa[1]] == posb:
                    Move(posa,posb)
        if (posb[0] - posa[0]) <= 0 and posa[1] == posb[1]: #Towards -ve x
            for i in range(1,posa[0] - posb[0]+1):
                if z[posa[0] - i][posa[1]][0] == True and (z[posa[0] - i][posa[1]][1] == 'w' or (z[posa[0] - i][posa[1]][1] == 'b' and [posa[0]-i,posa[1]] != posb)):
                    break
                if [posa[0] - i,posa[1]] == posb:
                    Move(posa,posb)
        if (posb[1] - posa[1]) > 0 and posa[0] == posb[0]: #Towards +ve y
            for i in range(1,posb[1]-posa[1]+1):
                if z[posa[0]][posa[1]+i][0] == True and (z[posa[0]][posa[1]+i][1] == 'w' or (z[posa[0]][posa[1]+i][1] == 'b' and [posa[0],posa[1]+i] != posb)):
                    break
                if [posa[0],posa[1]+i] == posb:
                    Move(posa,posb)
        if (posb[1] - posa[1]) <= 0 and posa[0] == posb[0]: #Towards -ve y
            for i in range(1,posa[1] - posb[1]+1):
                if z[posa[0]][posa[1]-i][0] == True and (z[posa[0]][posa[1]-i][1] == 'w' or (z[posa[0]][posa[1]-i][1] == 'b' and [posa[0],posa[1]-i] != posb)):
                    break
                if [posa[0],posa[1]-i] == posb:
                    Move(posa,posb)
        x = posb[0]-posa[0]
        y = posb[1] - posa[1]
        if x == -y and (x > 0 and y < 0): #Towards first quadrant
            for i in range(1,x+1):
                if z[posb[0]][posb[1]][0] == True and z[posb[0]][posb[1]][1] == 'w':
                    break
                if z[posa[0]+i][posa[1]-i][0] == True and (z[posa[0] + i][posa[1]-i][1] == 'w' or (z[posa[0] + i][posa[1]-i][1] == 'b' and [posa[0]+i,posa[1]-i] != posb)):
                    break
                if [posa[0]+i,posa[1]-i] == posb:
                    Move(posa,posb)
        if x == y and (x < 0 and y < 0): #Towards second quadrant
            for i in range(1,-x+1):
                if z[posb[0]][posb[1]][0] == True and z[posb[0]][posb[1]][1] == 'w':
                    break
                if z[posa[0]-i][posa[1]-i][0] == True and (z[posa[0] - i][posa[1]-i][1] == 'w' or (z[posa[0] - i][posa[1]-i][1] == 'b' and [posa[0]-i,posa[1]-i] != posb)):
                    break
                if [posa[0]-i,posa[1]-i] == posb:
                    Move(posa,posb)
        if x == -y and (x < 0 and y > 0): #Towards third quadrant
            for i in range(1,y+1):
                if z[posb[0]][posb[1]][0] == True and z[posb[0]][posb[1]][1] == 'w':
                    break
                if z[posa[0]-i][posa[1]+i][0] == True and (z[posa[0]-i][posa[1]+i][1] == 'w' or (z[posa[0] - i][posa[1]+i][1] == 'b' and [posa[0]-i,posa[1]+i] != posb)):
                    break
                if [posa[0]-i,posa[1]+i] == posb:
                    Move(posa,posb)
        if x == y and (x > 0 and y > 0): #Towards fourth quadrant
            for i in range(1,y+1):
                if z[posb[0]][posb[1]][0] == True and z[posb[0]][posb[1]][1] == 'w':
                    break
                if z[posa[0]+i][posa[1]+i][0] == True and (z[posa[0] + i][posa[1]+i][1] == 'w' or (z[posa[0] + i][posa[1]+i][1] == 'b' and [posa[0]+i,posa[1]+i] != posb)):
                    break
                if [posa[0]+i,posa[1]+i] == posb:
                    Move(posa,posb)

def moveBlackQueen(posa,posb):
    z = pickle.load(open( "data.bin",'rb'))
    if posa == posb: #Chechk if position a and b are same
        pass
    else:
        if posa[0] == posb[0] and (posb[1] - posa[1]) > 0: #Towards +ve y
            for i in range(1,posb[1]-posa[1]+1):
                if z[posa[0]][posa[1]+i][0] == True and (z[posa[0]][posa[1]+i][1] == 'b' or (z[posa[0]][posa[1]+i][1] == 'w' and [posa[0],posa[1]+i] != posb)):
                    break
                if [posa[0],posa[1]+i] == posb:
                    Move(posa,posb)
        if posa[0] == posb[0] and (posb[1] - posa[1]) <= 0: #Towards -ve y
            for i in range(1,posa[1] - posb[1]+1):
                if z[posa[0]][posa[1]-i][0] == True and (z[posa[0]][posa[1]-i][1] == 'b' or (z[posa[0]][posa[1]-i][1] == 'w' and [posa[0],posa[1]-i] != posb)):
                    break
                if [posa[0],posa[1]-i] == posb:
                    Move(posa,posb)
        if (posb[0] - posa[0]) > 0 and posa[1] == posb[1]: #Towards +ve x
            for i in range(1,posb[0]-posa[0]+1):
                if z[posa[0] + i][posa[1]][0] == True and (z[posa[0] + i][posa[1]][1] == 'b' or (z[posa[0] + i][posa[1]][1] == 'w' and [posa[0]+i,posa[1]] != posb)):
                    break
                if [posa[0] + i,posa[1]] == posb:
                    Move(posa,posb)
        if (posb[0] - posa[0]) <= 0 and posa[1] == posb[1]: #Towards -ve x
            for i in range(1,posa[0] - posb[0]+1):
                if z[posa[0] - i][posa[1]][0] == True and (z[posa[0] - i][posa[1]][1] == 'b' or (z[posa[0] - i][posa[1]][1] == 'w' and [posa[0]-i,posa[1]] != posb)):
                    break
                if [posa[0] - i,posa[1]] == posb:
                    Move(posa,posb)
        x = posb[0]-posa[0]
        y = posb[1] - posa[1]
        if x == -y and (x > 0 and y < 0): #Towards first quadrant
            for i in range(1,x+1):
                if z[posb[0]][posb[1]][0] == True and z[posb[0]][posb[1]][1] == 'b':
                    break
                if z[posa[0]+i][posa[1]-i][0] == True and (z[posa[0] + i][posa[1]-i][1] == 'b' or (z[posa[0] + i][posa[1]-i][1] == 'w' and [posa[0]+i,posa[1]-i] != posb)):
                    break
                if [posa[0]+i,posa[1]-i] == posb:
                    Move(posa,posb)
        if x == y and (x < 0 and y < 0): #Towards second quadrant
            for i in range(1,-x+1):
                if z[posb[0]][posb[1]][0] == True and z[posb[0]][posb[1]][1] == 'b':
                    break
                if z[posa[0]-i][posa[1]-i][0] == True and (z[posa[0] - i][posa[1]-i][1] == 'b' or (z[posa[0] - i][posa[1]-i][1] == 'w' and [posa[0]-i,posa[1]-i] != posb)):
                    break
                if [posa[0]-i,posa[1]-i] == posb:
                    Move(posa,posb)
        if x == -y and (x < 0 and y > 0): #Towards third quadrant
            for i in range(1,y+1):
                if z[posb[0]][posb[1]][0] == True and z[posb[0]][posb[1]][1] == 'b':
                    break
                if z[posa[0]-i][posa[1]+i][0] == True and (z[posa[0]-i][posa[1]+i][1] == 'b' or (z[posa[0] - i][posa[1]+i][1] == 'w' and [posa[0]-i,posa[1]+i] != posb)):
                    break
                if [posa[0]-i,posa[1]+i] == posb:
                    Move(posa,posb)
        if x == y and (x > 0 and y > 0): #Towards fourth quadrant
            for i in range(1,y+1):
                if z[posb[0]][posb[1]][0] == True and z[posb[0]][posb[1]][1] == 'b':
                    break
                if z[posa[0]+i][posa[1]+i][0] == True and (z[posa[0] + i][posa[1]+i][1] == 'b' or (z[posa[0] + i][posa[1]+i][1] == 'w' and [posa[0]+i,posa[1]+i] != posb)):
                    break
                if [posa[0]+i,posa[1]+i] == posb:
                    Move(posa,posb)


def Move(posa,posb):
    v = pickle.load(open( "data.bin",'rb'))
    if v[posa[0]][posa[1]][1] == 'b':
        v[posb[0]][posb[1]][1] = 'b'
    else:
        v[posb[0]][posb[1]][1] = 'w'
    v[posb[0]][posb[1]][0] = True
    v[posb[0]][posb[1]][2] = 'q'
    v[posa[0]][posa[1]][0] = False
    pickle.dump(v, open('data.bin','wb'))
    changeTurn()
    import Scripts.pawn as p
    p.enpassant[0] = False