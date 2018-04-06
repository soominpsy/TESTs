def fibo_s(num):
    if(num==1 or num==2):
        return 1
    else:
        return fibo_s(num-2)+fibo_s(num-1)

def fibo_p(num):
    for i in range(1,num+1):
        print(fibo_s(i),"",end="")

fibo_p(10)
