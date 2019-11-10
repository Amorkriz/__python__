def getC(R,G,B):
    count = [0 for _ in range(8)]
    if R==0:
        i=0
    else:
        i = (R//10)+1
    if G==0:
        j=0
    else:
        j = (G//10)+1
    if B==0:
        k=0
    else:
        k = (B//10)+1
    if ((k%2==0)&(j%2==0)&(i%2==0)):
        count[0] += 1
    if ((k%2==0)&(j%2==0)&(i%2==1)):
        count[1] += 1
    if ((k%2==0)&(j%2==1)&(i%2==0)):
        count[2] += 1
    if ((k%2==0)&(j%2==1)&(i%2==1)):
        count[3] += 1
    if ((k%2==1)&(j%2==0)&(i%2==0)):
        count[4] += 1
    if ((k%2==1)&(j%2==0)&(i%2==1)):
        count[5] += 1
    if ((k%2==1)&(j%2==1)&(i%2==0)):
        count[6] += 1
    if ((k%2==1)&(j%2==1)&(i%2==1)):
        count[7] += 1
    C = count.index(1)
    return C




count = [0 for _ in range(8)]
C = [[] for _ in range(8)]
for i in range(27):
    for j in range(27):
        for k in range(27):
            if ((k%2==0)&(j%2==0)&(i%2==0)):
                count[0] += 1
                ijk = str(i)+' '+str(j)+' '+str(k)
                C[0].append(ijk)
            if ((k%2==0)&(j%2==0)&(i%2==1)):
                count[1] += 1
                ijk = str(i)+' '+str(j)+' '+str(k)
                C[1].append(ijk)
            if ((k%2==0)&(j%2==1)&(i%2==0)):
                count[2] += 1
                ijk = str(i)+' '+str(j)+' '+str(k)
                C[2].append(ijk)
            if ((k%2==0)&(j%2==1)&(i%2==1)):
                count[3] += 1
                ijk = str(i)+' '+str(j)+' '+str(k)
                C[3].append(ijk)
            if ((k%2==1)&(j%2==0)&(i%2==0)):
                count[4] += 1
                ijk = str(i)+' '+str(j)+' '+str(k)
                C[4].append(ijk)
            if ((k%2==1)&(j%2==0)&(i%2==1)):
                count[5] += 1
                ijk = str(i)+' '+str(j)+' '+str(k)
                C[5].append(ijk)
            if ((k%2==1)&(j%2==1)&(i%2==0)):
                count[6] += 1
                ijk = str(i)+' '+str(j)+' '+str(k)
                C[6].append(ijk)
            if ((k%2==1)&(j%2==1)&(i%2==1)):
                count[7] += 1
                ijk = str(i)+' '+str(j)+' '+str(k)
                C[7].append(ijk)
R,G,B = 209,115,56
if R==0:
    i=0
else:
    i = (R//10)+1
if G==0:
    j=0
else:
    j = (G//10)+1
if B==0:
    k=0
else:
    k = (B//10)+1
string = str(i)+' '+str(j)+' '+str(k)
n = getC(R,G,B)
ls = C[n].index(string)
'''
这个文件可以通过输出RGB找到对应的C几块中的第几个是该RGB的增益
'''
print(n,ls)