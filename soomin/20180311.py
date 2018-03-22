x=[251, 357, 82, 136, 62]

def maximum(x):                             
    for i in range (len(x)):                   # for command, from 'i' to 'x length'
        for j in range(len(x)-i):              # Since from the first circulation, the maximum number move to the las place,set range to len(x)-1 
            k=0
            if j<4:                            # if j+1 is over than len(x), it shows error.
                if x[j]>x[j+1]:
                    k=x[j]                     #swap 
                    x[j]=x[j+1]
                    x[j+1]=k
                    
                else:
                    continue
    print(x)


maximum(x)
