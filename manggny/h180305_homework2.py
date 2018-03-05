# return a list where the smaller number is first
def return_list(a,b):
    if a<=b:
        l = [a,b]
    else:
        l = [b,a]
    return l

def main(x):
    for i in range(len(x)):
        for j in range(i,len(x)):
            min = return_list(x[i],x[j])
            x[i],x[j] = min[0],min[1]

    print(x)

x= [125,421,327,380,728,645]

main(x)

