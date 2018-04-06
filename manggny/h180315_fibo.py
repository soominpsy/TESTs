def jaegui(num): # 재귀 함수입니다.
    if num == 1: # 만약 1이면 1을 반환합니다.
        return 1
    elif num <=0: # 만약 参数가 0보다 작거나 같으면 0을 반환합니다.
        return 0
    return jaegui(num-1)+jaegui(num-2)  # 전과 전전 수열 값의 합을 더한값을 반환합니다.

def fibo(num):   # 피보나치 수열입니다.
    for i in range(num): # num만큼 반복해줍니다.
        print(jaegui(i+1)) #i+1만큼 값의 재귀함수 값을 출력해줍니다.
    return 0 # 형식상..
fibo(10) # 10번째까지 피보나치 수열입니다.
