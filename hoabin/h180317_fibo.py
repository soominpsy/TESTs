#--coding: UTF-8--

def jaegui(num): # 피보나치 수열 만드는 재귀함수 정의
    if num == 1: # 첫번째 수열
        return 1
    elif num == 0: # 0번째 수열
        return 0
    else:          # 두번째 이상일시 전수열과 전전수열 합산
        return jaegui(num-2)+jaegui(num-1)

def fibo(x): # 피보나치 수열 함수
    for k in range(1,x+1): # 1부터 주어진 숫자순만큼 반복
        A=jaegui(k) # k번째 수열
        print(A) # k번째 수열 출력

fibo(7)
