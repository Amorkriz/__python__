import re
import numpy as np
import os


def ReadTxtName(rootdir):
    '''
    这个函数输入的是海思工具生成的表
    得到的是一个长度为546的一维列表，每个元素含义代表一行的9个数字，tpye是str
    '''
    lines = []
    with open(rootdir, 'r') as file_to_read:
        while True:
            line = file_to_read.readline()
            if not line:
                break
            line = line.strip('\n')[:-1]
            lines.append(line)
    return lines

def getC_RGB(R,G,B):
    '''
    这个函数可以通过输入RGB的值获得该RGB值的表块是多少（C[0]到C[7]中的一个）
    '''
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

def getC_ijk(i,j,k):
    '''
    这个函数可以通过输入ijk的值获得该RGB值的表块是多少（C[0]到C[7]中的一个）
    '''
    count = [0 for _ in range(8)]
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

def getCnums(i_,j_,k_):
    '''
    输入i,j,k,得到的是在大块中的序列
    '''
    count = [0 for _ in range(8)]
    C = [[] for _ in range(8)]
    for k in range(17):
        for j in range(17):
            for i in range(17):
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
    string = str(i_)+' '+str(j_)+' '+str(k_)
    n = getC_ijk(i_,j_,k_)
    ls = C[n].index(string)
    return ls

def getijk(R,G,B):
    '''
    输入的是RGB值
    返回的是这个像素值在三维空间中排布到具体哪一块（一共是27*27*27块）
    例如：temp = getijk(201,56,94)，返回的是一个元组(21, 6, 10)
    '''
    i,j,k = -1,-1,-1
    if R==0:#这里还需要讨论，因为要分成27块，而给出的27个数字包含首尾（0和255），中间相隔26块，我把0单独作为一块，{1，2，3，4，5，6，7，8，9}在第二块，以此类推
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
    return i,j,k

def getRGB__(n,nums):
    '''
    输入的是第n大块，是这块中的第nums个数字
    返回的是在txt中第多少行，以及在这行里第几个
    例如：
        getRGB__(0,0)         (0, 0)
        getRGB__(0,1)         (0, 1)
        getRGB__(0,2743)      (342, 7)
        getRGB__(1,2744)      (343, 0)
        getRGB__(2,5292)      (661, 0)
    '''
    ln = [0,343,319,319,296,319,296,296]#275
    diff = [0,0,4,4,2,4,2,2]
    temp1 = 0#个数
    temp2 = 0#行数
    for _ in range(n+1):
        # temp1 += ln[_]*8
        temp1 += diff[_]
        temp2 += ln[_]
    # nums = nums - temp1
    a = nums // 8 + temp2 
    b = nums%8
    return a,b

def ln2words(list_):
    '''
    输入处理为一行一行的列表
    返回二维数组,第二维里面是30位的二进制数字，type是str
    '''
    ori = []
    n = len(list_)
    for _ in range(n):#循环结束后，ori成为一个二维数组，把每一行的lut再作为一个列表，里面的9个30位二进制是元素
        lnx = []
        lnx = re.split(r',\s',list_[_])
        res = []
        for k in range(len(lnx)):
            temp = lnx[k].split()
            tem = "".join(temp)
            res.append((bin(int(tem)).replace('0b','')).rjust(30,'0'))
        ori.append(res)
    return ori

def getN_lines(_):
    temo = [0,80,152,224,288,360,424,488,545]
    k = 0
    while True:
        if _ <= temo[k+1]:
            break
        else:
            k += 1
    return k

def transfer(words):
    R = [[] for _ in range(8)]
    G = [[] for _ in range(8)]
    B = [[] for _ in range(8)]
    for _ in range(len(words)):
        for __ in range(len(words[_])):
            tempR,tempG,tempB = words[_][__][20:30],words[_][__][10:20],words[_][__][0:10]
            mR,mG,mB = uint2int(tempR),uint2int(tempG),uint2int(tempB)
            R[getN_lines(_)].append(mR)
            G[getN_lines(_)].append(mG)
            B[getN_lines(_)].append(mB)
    return R,G,B

# def uint2int(words):
#     temp = words[1:10]
#     if words[0] == '1':
#         m = -int(temp,2)
#     else:
#         m = int(temp,2)
#     return m

def add_1(binary_inpute):#二进制编码加1
    _,out = bin(int(binary_inpute,2)+1).split("b")
    return out

def reverse(binary_inpute):#取反操作
    binary_inpute = list(binary_inpute)
    binary_out = binary_inpute
    for epoch,i in enumerate(binary_out):
        if i == "0":
            binary_out[epoch] = "1"
        else:
            binary_out[epoch] = "0"
    return "".join(binary_out)

def uint2int(a):
    if a[0] == "1":#判断为负数
        a_reverse = reverse(a[1:])  # 取反
        a_add_1 = add_1(a_reverse)  # 二进制加1
        a_int = -int(a_add_1, 2)
    else:
        a_int = int(a[1:])
    return a_int