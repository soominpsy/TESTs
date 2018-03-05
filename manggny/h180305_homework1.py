def times(x): #5의 배수를 출력하는 함수를 만드려 합니다. X는 리스트 형식입니다.
    for i in range(len(x)): #X의 길이만큼 순환해 줍니다. 0~len(x)-1
        if x[i]%5 == 0: # 만약 x리스트의 i번째 데이터가 5의 배수이면 프린트합니다.
            print(x[i])
        else:
            continue # 아니면 순환을 계속합니다.

x= [125,421,327,380,728,645]

times(x)
