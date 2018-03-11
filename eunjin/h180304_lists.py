#-*-coding: UTF-8-*-

a=[125,421,327,380,728,645]
li= [] 
for i in range(6):
    if a[i]%5==0:
        li.append(a[i])     
print(li)

#1
for i in range(0,5):        #앞에 원소와 뒤에원소를 비교함
    for j in range(i+1,6):
        if (a[i]>a[j]):     #앞에 원소가 더 크면 일단 다른곳에다 저장후 
            k = a[i]        # 뒤에 원소를 앞으로 옮기고 뒤자리에 큰걸둠
            a[i] = a[j]     #매자리끼리 서로비교
            a[j] =k

print(a)

#2
b=[125,421,327,380,728,645]
list.sort(b)    #작은수부터 나열하는 함수
print(b)
