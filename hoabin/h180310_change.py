#1 순서바꾸기
a = 4
b = 9
k = a
a= b
b = k

print (a, b)

#2 작은수부터 정렬하기
X = [251, 357, 82, 136, 62]

for n in range(len(X)): #반복범위 설정
    for i in range(0,len(X)-n): #비교범위 설정
        if i+1 >= len(X)-n: #index 범위 벗어나는 오류 발생전에 반복문 끝내기
            break

        if X[i] > X[i+1]: # 앞자리와 뒷자리 수 비교
            k = X[i]      # 앞자리 수가 큰경우 뒷자리 수와 자리 변경
            X[i] = X[i+1]
            X[i+1] = k

print (X) # 결과물 출력