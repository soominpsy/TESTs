#-*-coding: UTP-8-*-
Num=[125,421,327,380,728,645]

def Mulf(a):                #5의 배수를 찾는 함수
    for i in range(len(a)): #len함수는 list의 길이를 구하는 함수입니다
        if(a[i]%5==0):      #5로 나눠서 나머지가 0이 되는 수는 5의 배수
            print(a[i])     #5의 배수를 하나씩 출력

def Mtmf(b):                #list내 최소값-최대값 순서로 출력하는 함수
    cc=0                    #본 코드에서 cc변수는 list내 원소 자리를 저장
    k=1                     #len함수에 k값을 그대로 사용하면 아래 코드에러발생
    Min=int(b[k-1])         #list의 첫번째 자리를 최소값으로 설정하고 시작
    for k in range(len(b)): #k=1, 첫 시작은 list내 0번과 1번의 비교
        if(Min<int(b[k])):  #int함수를 이용한 정수 변환, 비교
            continue        #최소값이 그대로 작다면 계속
        else:
            Min=int(b[k])   #아니라면 최소값을 수정하고 그 위치를 저장
            cc=k
    print(Min)              #최소값 출력
    del b[cc]               #아래의 재귀함수 이용을 위한 최소값 제거
    if(len(b)!=0):          #list의 길이가 0과 다를때 본 함수는 계속 실행됨
        Mtmf(b)             #본 함수는 자기자신을 불러들이는 재귀함수
        
Mulf(Num)
print("\n")
Mtmf(Num)
