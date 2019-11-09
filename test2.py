import re
import numpy as np


def ReadTxtName(rootdir):
    lines = []
    with open(rootdir, 'r') as file_to_read:
        while True:
            line = file_to_read.readline()
            if not line:
                break
            line = line.strip('\n')
            lines.append(line)
    return lines

ln = ReadTxtName('LUTBIN2.txt')

bin = []
for _ in range(2463):
    lnx = []
    lnx =  re.split(r'\s',ln[_])
    bin.append(lnx)

# print(np.shape(bin))        (2463, 9)

R=[]
G=[]
B=[]
for _ in range(2463):
    Rbin=[]
    Gbin=[]
    Bbin=[]
    Rbin_0 = bin[_][0][20:32]
    Gbin_0 = bin[_][0][8:20]
    Bbin_0 = bin[_][1][28:32]+bin[_][0][0:8]
    Rbin.append(Rbin_0)
    Gbin.append(Gbin_0)
    Bbin.append(Bbin_0)

    Rbin_1 = bin[_][1][16:28]
    Gbin_1 = bin[_][1][4:16]
    Bbin_1 = bin[_][2][24:32]+bin[_][1][0:4]
    Rbin.append(Rbin_1)
    Gbin.append(Gbin_1)
    Bbin.append(Bbin_1)

    Rbin_2 = bin[_][2][12:24]
    Gbin_2 = bin[_][2][0:12]
    Bbin_2 = bin[_][3][20:32]
    Rbin.append(Rbin_2)
    Gbin.append(Gbin_2)
    Bbin.append(Bbin_2)

    Rbin_3 = bin[_][3][8:20]
    Gbin_3 = bin[_][4][28:32]+bin[_][3][0:8]
    Bbin_3 = bin[_][4][16:28]
    Rbin.append(Rbin_3)
    Gbin.append(Gbin_3)
    Bbin.append(Bbin_3)

    Rbin_4 = bin[_][4][4:16]
    Gbin_4 = bin[_][5][24:32]+bin[_][4][0:4]
    Bbin_4 = bin[_][5][12:24]
    Rbin.append(Rbin_4)
    Gbin.append(Gbin_4)
    Bbin.append(Bbin_4)

    Rbin_5 = bin[_][5][0:12]
    Gbin_5 = bin[_][6][20:32]
    Bbin_5 = bin[_][6][8:20]
    Rbin.append(Rbin_5)
    Gbin.append(Gbin_5)
    Bbin.append(Bbin_5)

    Rbin_6 = bin[_][7][28:32]+bin[_][6][0:8]
    Gbin_6 = bin[_][7][16:28]
    Bbin_6 = bin[_][7][4:16]
    Rbin.append(Rbin_6)
    Gbin.append(Gbin_6)
    Bbin.append(Bbin_6)

    Rbin_7 = bin[_][8][24:32]+bin[_][7][0:4]
    Gbin_7 = bin[_][8][12:24]
    Bbin_7 = bin[_][8][0:12]
    Rbin.append(Rbin_7)
    Gbin.append(Gbin_7)
    Bbin.append(Bbin_7)
    
    Rdec=[]
    Gdec=[]
    Bdec=[]
    for _ in range(8):
        temp1 = int(Rbin[_],2)
        Rdec.append(temp1)
        temp2 = int(Gbin[_],2)
        Gdec.append(temp2)
        temp3 = int(Bbin[_],2)
        Bdec.append(temp3)
    
    R.append(Rdec)
    G.append(Gdec)
    B.append(Bdec)

print(R)
print(G)
print(B)