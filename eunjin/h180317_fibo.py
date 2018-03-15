#--coding:UTF-8--

def fibo(i):
    if i == 1 or i == 2:  #첫번째와 두번째는 1 출력
        return 1
    else:
        return fibo(i-2) + fibo(i-1) #3번째부터는 그 앞 두개를 더함

for i in range(1,8):
    print(fibo(i))
