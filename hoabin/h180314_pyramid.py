#1 별표 피라미드 만들기 함수

def pyramid1(n): # 별표 피라미드 함수
    for a in range (n): # 입력한 숫자에 따른 범위
        P=["*" for a in range (n)] # 주어진 범위에 따른 별표 리스트 만들기
        for b in range (a+2): # 각 단별로 리스트 나누기 위한 반복문// 왜 +2를 해야하죠?? +2 안하면 공백이 두번 나와요...
            P1=[P[b] for b in range (b)] # 단별 리스트
        print(P1) # 출력

#2 숫자 피라미드 만들기 함수
def pyramid2(n): # 숫자 피라미드 함수
    for a in range (n): # 입력한 숫자에 따른 범위
        P=[a+1 for a in range (n)] # 주어진 범위에 따른 숫자 리스트 만들기
        for b in range (a+2): # 각 단별로 나누기 위한 반복문
            P2=[P[b] for b in range (b)] # 단별 리스트
        print (P2) # 출력


pyramid1(5)
pyramid2(7)