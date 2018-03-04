Num=[125,421,327,380,728,645]

def Mulf(a):
    for i in range(len(a)):
        if(a[i]%5==0):
            print(a[i])

def MtMf(a):
    k=1
    cc=0
    Min=int(a[k-1])
    for k in range(len(a)):
        if(Min<int(a[k])):
            continue
        else:
            Min=int(a[k])
            cc=k
    print(Min)
    del a[cc]
    if(len(a)!=0):
        MtMf(a)


Mulf(Num)
print("\n")
MtMf(Num)
