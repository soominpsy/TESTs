#1
a=4
b=8
print("a,b=",a,b)

t=a #a값을 t에 저장
a=b #b값을 a에
b=t #t값을 b에

print("after a,b = ",a,b)

#2
c=6
d=2
if c>d:
    k=c
    c=d
    d=k
print(c,d)

#3 저번숙제할때 썻던방법
x=[251,357,82,136,62]
for i in range(len(x)):
    for j in range(1,len(x)):
        m = x[i]
        x[i]=x[j]
        x[j]=m
print(x)

