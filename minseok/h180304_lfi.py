Num=[125,421,327,380,728,645]

def Mulf(a):
    for i in range(len(a)):
        if(a[i]%5==0):
            print(a[i])

def MtMf(a):
    k=1
    cc=0
    Max=int(a[k-1])
    for k in range(len(a)):
        if(Max>int(a[k])):
            continue
        else:
            Max=int(a[k])
            cc=k
    print(Max)
    del a[cc]
    if(len(a)!=0):
        MtMf(a)


Mulf(Num)
print("\n")
MtMf(Num)
