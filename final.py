import re
import numpy as np
import os
import xlwt
import openpyxl


from __function__ import ReadTxtName
from __function__ import getC_RGB
from __function__ import getC_ijk
from __function__ import getCnums
from __function__ import getijk
from __function__ import getRGB__
from __function__ import ln2words
from __function__ import transfer


ln = ReadTxtName('lut_ori.txt')
words = ln2words(ln)#words是一个二维数组
R = transfer(words)[0]
G = transfer(words)[1]
B = transfer(words)[2]

deltaR,deltaG,deltaB = [],[],[]
for _ in range(17):
    for __ in range(17):
        for ___ in range(17):
            tmp = getC_ijk(_,__,___)
            nums = getCnums(_,__,___)
            deltaR.append(int(R[tmp][nums] / 32))
            deltaG.append(int(G[tmp][nums] / 32))
            deltaB.append(int(B[tmp][nums] / 32))
print(np.shape(deltaB))
print(len(deltaB))



'''''''''''''''''''''''''''''''''''''''''生成excel'''''''''''''''''''''''''''''''''''''''''
f = xlwt.Workbook()
sheet1 = f.add_sheet('lut',cell_overwrite_ok=True)

colum1 = [[k for _ in range(289)] for k in [_ for _ in range(255)][0:255:16] + [255]]
colum2_tmp,colum2 = [],[]
for k in range(0,255,16):#271=255+16
    colum2_tmp += [k for _ in range(17)]
colum2_tmp += [255 for i in range(17)]
for _ in range(17):
    colum2 += colum2_tmp
colum3 = [([_ for _ in range(255)][0:255:16] + [255]) for i in range(289)]

#写第一列
m1 = 0
for k in range(17):
    for i in range(289):
        sheet1.write(i+m1,0,colum1[k][i])
    m1 += 289

#写第二列
for _ in range(4913):
    sheet1.write(_,1,colum2[_])

#写第三列
m3 = 0
for k in range(289):
    for i in range(17):
        sheet1.write(i+m3,2,colum3[k][i])
    m3 += 17

for k in range(4913):
    sheet1.write(k,3,deltaR[k])
for k in range(4913):
    sheet1.write(k,4,deltaG[k])
for k in range(4913):
    sheet1.write(k,5,deltaB[k])

f.save('test.xls')