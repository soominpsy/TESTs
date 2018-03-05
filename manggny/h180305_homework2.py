# 이 함수는 a,b 두가지 int형식의 변량을 넣으면 길이가 2 인 list를 리턴하는 함수입니다.
# 메인 함수에서 숫자 크기에 따라 위치를 바꿀때 사용할 것 입니다.
def return_list(a,b):
    if a<=b: # a가 작거나 같으면 리스트 ㅣ은 [a,b]
        l = [a,b]
    else:
        l = [b,a] # 그외에 l 은 [b,a]
    return l #l을 반환해 줍니다.

def main(x): # 주 함수입니다.
    for i in range(len(x)): # x길이만큼 순환합니다.
        for j in range(i,len(x)): # i에서 시작해서 x길이까지 순환합니다(i가 2이면, j는 2~x길이)
            min = return_list(x[i],x[j]) # 리턴 리스트 함수를 사용해서 min이라는 리스트 변량에 값을 부여합니다.
            x[i],x[j] = min[0],min[1] # min의 부여된 값을 다시 x에 넣어서 자리 변환을 완성합니다.

    print(x) # 프린트

x= [125,421,327,380,728,645]

main(x)

