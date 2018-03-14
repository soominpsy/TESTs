def py1(num):                           # $피라미드 함수 정의
    for i in range(num):                # 첫순환, [0~(num-1)]순환
            for k in range(num):        # 두번째 순환, num범위 순환
                print("$",end="")       # $출력, end=""를 이용한 줄바꿈 방지
                if(k==i):               # k가 i와 같다면
                    print("")           # ""을 출력해서 줄바꿈
                    break               # 순환을 빠져나오고, i와k는 0으로 리셋

def py2(num):                           # 숫자 피라미드 함수 정의
    for i in range(1,num+1):            # 첫순환, 1~num까지의 순환
            for k in range(1,num+1):    # 두번째 순환, 1~num까지의 순환
                print(k,end="")         # 정수 k 출력, end=""를 이용한 이어쓰기
                if(k==i):               # k가 i와 같을 때
                    print("")           # ""를 이용한 줄바꿈
                    break               # 순환을 탈출, i와 k는 0으로 리셋

py1(5)
py2(7)
