a=[125,421,327,380,728,645]
li= [] 
for i in range(6):
    if a[i]%5==0:
        li.append(a[i])     
print(li)

#1
for i in range(0,5):
    for j in range(i+1,6):
        if (a[i]>a[j]):
            k = a[i]
            a[i] = a[j]
            a[j] =k

print(a)

#2
b=[125,421,327,380,728,645]
list.sort(b)
print(b)
