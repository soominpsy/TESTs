#-*-coding: UTF-8-*-
Num=[125,421,327,380,728,645]

def Mulf(a):
    for i in range(len(a)):
        if(a[i]%5==0):
            print(a[i])
#for과 if 및 %를 사용해 5의 배수 찾기
#len함수는 list의 길이를 구하는 함수

def MtMf(a):
    k=1
    cc=0
    Min=int(a[k-1])
    for k in range(len(a)):
        if(Min<int(a[k])):
            continue
        else:
            Min=int(a[k])
            cc=k
    print(Min)
    del a[cc]
    if(len(a)!=0):
        MtMf(a)
#int함수를 이용한 정수화
'''
for k in range(len(a)):
    if(int(a[k])<int(a[k+1])):
'''
#위와 같은 상황은 리스트 길이초과 에러가 나온다
#cc변수로 최소값의 위치를 저장, del을 사용하여 해당위치 원소 삭제
#!=0을 이용하여 list의 길이가 0보다 클때 자기자신을 다시 불러들임

Mulf(Num)
print("\n")
MtMf(Num)
