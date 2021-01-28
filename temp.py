import pickle

#Dump all the default data at the start of the game
c=[[[False,"b","p"],[False,"b","p"],[False,"b","p"],[False,"b","p"],[False,"b","p"],[False,"b","p"],[False,"b","p"],[False,"b","p"]],[[False,"b","p"],[False,"b","p"],[False,"b","p"],[False,"b","p"],[False,"b","p"],[False,"b","p"],[False,"b","p"],[False,"b","p"]],[[False,"b","p"],[False,"b","p"],[False,"b","p"],[False,"b","p"],[False,"b","p"],[False,"b","p"],[False,"b","p"],[False,"b","p"]],[[False,"b","p"],[False,"b","p"],[False,"b","p"],[False,"b","p"],[False,"b","p"],[False,"b","p"],[False,"b","p"],[False,"b","p"]],[[False,"b","p"],[False,"b","p"],[False,"b","p"],[False,"b","p"],[False,"b","p"],[False,"b","p"],[False,"b","p"],[False,"b","p"]],[[False,"b","p"],[False,"b","p"],[False,"b","p"],[False,"b","p"],[False,"b","p"],[False,"b","p"],[False,"b","p"],[False,"b","p"]],[[False,"b","p"],[False,"b","p"],[False,"b","p"],[False,"b","p"],[False,"b","p"],[False,"b","p"],[False,"b","p"],[False,"b","p"]],[[False,"b","p"],[False,"b","p"],[False,"b","p"],[False,"b","p"],[False,"b","p"],[False,"b","p"],[False,"b","p"],[False,"b","p"]]]

pickle.dump(c,open("data.bin",'wb'))
pickle.dump(False,open("turn.bin",'wb'))

#Make entries of the pawns
a = pickle.load(open("data.bin",'rb'))

for i in range(8):
    a[i][1][0] = True
    a[i][1][1] = "b"
    a[i][1][2] = "p"
    a[i][6][0] = True
    a[i][6][1] = "w"
    a[i][6][2] = "p"

pickle.dump(a, open("data.bin","wb"))


#Make entries in data for position of black king
a[4][0][0] = True
a[4][0][1] = "b"
a[4][0][2] = 'ki'

#Make enteries in data for positions of white king
a[4][7][0] = True
a[4][7][1] = "w"
a[4][7][2] = 'ki'

pickle.dump(a,open('data.bin','wb'))

a = pickle.load(open("data.bin",'rb'))

#Make entries in data for position of black knights
a[1][0][0] = True
a[1][0][1] = "b"
a[1][0][2] = 'kn'
a[6][0][0] = True
a[6][0][1] = "b"
a[6][0][2] = 'kn'

#Make enteries in data for positions of white knights
a[1][7][0] = True
a[1][7][1] = "w"
a[1][7][2] = 'kn'
a[6][7][0] = True
a[6][7][1] = "w"
a[6][7][2] = 'kn'

pickle.dump(a,open('data.bin','wb'))

a = pickle.load(open("data.bin",'rb'))

#Make entries in data for position of black bishops
a[2][0][0] = True
a[2][0][1] = "b"
a[2][0][2] = 'b'
a[5][0][0] = True
a[5][0][1] = "b"
a[5][0][2] = 'b'

#Make enteries in data for positions of white bishops
a[2][7][0] = True
a[2][7][1] = "w"
a[2][7][2] = 'b'
a[5][7][0] = True
a[5][7][1] = "w"
a[5][7][2] = 'b'

pickle.dump(a,open('data.bin','wb'))

a = pickle.load(open("data.bin",'rb'))

#Make entries in data for position of black queen
a[3][0][0] = True
a[3][0][1] = "b"
a[3][0][2] = 'q'

#Make enteries in data for positions of white queen
a[3][7][0] = True
a[3][7][1] = "w"
a[3][7][2] = 'q'

pickle.dump(a,open('data.bin','wb'))


a = pickle.load(open("data.bin",'rb'))

#Make entries in data for position of black rooks
a[0][0][0] = True
a[0][0][1] = "b"
a[0][0][2] = 'r'
a[7][0][0] = True
a[7][0][1] = "b"
a[7][0][2] = 'r'

#Make enteries in data for positions of white rooks
a[0][7][0] = True
a[0][7][1] = "w"
a[0][7][2] = 'r'
a[7][7][0] = True
a[7][7][1] = "w"
a[7][7][2] = 'r'

pickle.dump(a,open('data.bin','wb'))