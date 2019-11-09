count = [0 for _ in range(8)]
for i in range(27):
    for j in range(27):
        for k in range(27):
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
print(count)