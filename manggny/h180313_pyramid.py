#-*-coding: UTF-8-*-
# 첫번째 숙제 별 피라미드
def pyramid(n): #n만큼 만듦
    k = "*" # k초기값
    for i in range(n): #n번 순환
        print(k) #k 출력
        k += "*" # 출력 후 k에 *을 하나 더 붙임

pyramid(5)# 함수 진행

#두번째 숫자 피라미드
def pyramin_num(n): #숫자 피라미드 함수 정의
    k = "1" #k는 스트링 형식의 1로 초기값 설정
    for i in range(2,n+2): # 2~n+1까지의 순환  
        print(k) # k 를 출력
        k += str(i) # k뒤에 i의 스트링 형식 붙이기

pyramin_num(7) #함수 진행
