#1
def pyramid1(n):
    for i in range(n+1): 
        print("*"*i)      #매반복마다 i만큼 곱한*를 print


#2
def pyramid2(m):
    i,j=0,0
    while i <m:
        i=i+1
        while j<i:
            j=j+1
            print(j,end=" ") #end 줄바꿈이 일어나지않게함
        print("\n")  #한줄띄우기
        j=0


pyramid1(5)
pyramid2(7)
