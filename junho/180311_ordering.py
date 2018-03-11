a = [251, 357, 82, 136, 62]

def ordering(x):
    for i in range(len(x)):             # loop all of the elements
        for j in range(len(x)-i):      # setting range from 0 to before lastest setting of biggest value
            if j < 4:
                if x[j]>x[j+1]:
                    k=x[j]              #swap two of them if later is smaller than beginner
                    x[j] = x[j+1]
                    x[j+1] = k
                else:
                    continue

ordering(a)
print(a)

