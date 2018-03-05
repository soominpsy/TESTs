Num=[125,421,327,380,728,645]

def Mulf(a):
    for i in range(len(a)):
        if(a[i]%5==0):
            print(a[i])

def Mtmf(b):
    cc=0
    k=1
    Min=int(b[k-1])
    for k in range(len(b)):
        if(Min<int(b[k])):
            continue
        else:
            Min=int(b[k])
            cc=k
    print(Min)
    del b[cc]
    if(len(b)!=0):
        Mtmf(b)
        
Mulf(Num)
print("\n")
Mtmf(Num)
