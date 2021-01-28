import pickle


def changeTurn():
    z = pickle.load(open("turn.bin",'rb'))
    if z == True:
        pickle.dump(False,open("turn.bin",'wb'))
    else:
        pickle.dump(True,open("turn.bin",'wb'))

def moveBlackKnight(posa,posb):
    z = pickle.load(open("data.bin",'rb'))
    x = posb[0]-posa[0]
    y = posb[1]-posa[1]
    if ([x,y] == [1,2] or [x,y] == [-1,2] or [x,y] == [-2,1] or [x,y] == [-2,-1] ) and (z[posb[0]][posb[1]][0] == False or z[posb[0]][posb[1]][1] == 'w' ):
        Move(posa,posb)
    if ([x,y] == [-1,-2] or [x,y] == [1,-2] or [x,y] == [2,-1] or [x,y] == [2,1] ) and (z[posb[0]][posb[1]][0] == False or z[posb[0]][posb[1]][1] == 'w' ):
        Move(posa,posb)

def moveWhiteKnight(posa,posb):
    z = pickle.load(open("data.bin",'rb'))
    x = posb[0]-posa[0]
    y = posb[1]-posa[1]
    if ([x,y] == [1,2] or [x,y] == [-1,2] or [x,y] == [-2,1] or [x,y] == [-2,-1] ) and (z[posb[0]][posb[1]][0] == False or z[posb[0]][posb[1]][1] == 'b' ):
        Move(posa,posb)
    if ([x,y] == [-1,-2] or [x,y] == [1,-2] or [x,y] == [2,-1] or [x,y] == [2,1] ) and (z[posb[0]][posb[1]][0] == False or z[posb[0]][posb[1]][1] == 'b' ):
        Move(posa,posb)


def Move(posa,posb):
    v = pickle.load(open( "data.bin",'rb'))
    if v[posa[0]][posa[1]][1] == 'b':
        v[posb[0]][posb[1]][1] = 'b'
    else:
        v[posb[0]][posb[1]][1] = 'w'
    v[posb[0]][posb[1]][0] = True
    v[posb[0]][posb[1]][2] = 'kn'
    v[posa[0]][posa[1]][0] = False
    pickle.dump(v, open('data.bin','wb'))
    changeTurn()
    import Scripts.pawn as p
    p.enpassant[0] = False