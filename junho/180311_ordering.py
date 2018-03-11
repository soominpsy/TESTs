a = [251, 357, 82, 136, 62]

def ordering(x):
    for i in range(len(x)):
        for j in range(len(x)-i):
            if j < 4:
                if x[j]>x[j+1]:
                    k=x[j]
                    x[j] = x[j+1]
                    x[j+1] = k
                else:
                    continue

ordering(a)
print(a)

