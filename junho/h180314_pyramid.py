from __future__ import print_function  # this is use for priting without change line

def PrintStar(n):
    for i in range(n):
        temp1 = n-i-1
        temp2 = n+i-1
        for j in range(2*n-1):
            if(i==0): 
                if(j==temp1):
                    print("*", end='')
                else:
                    print(" ", end='')
            else :
                if(temp1==j & temp1<=temp2):
                    print("*", end='')
                    temp1 = temp1+2
                else: 
                    print(" ", end='')
        print(" ")

def PrintNums(n):
    for i in range(n):
        temp1 = n-i-1
        temp2 = n+i-1
        kk = 1
        for j in range(2*n-1):
            if(i==0):
                if(j==temp1):
                    print(1, end='')
                else:
                    print(" ", end='')
            else :
                if(temp1==j & temp1<=temp2):
                    print(kk, end='')
                    kk = kk+1
                    temp1 = temp1+2
                else:
                    print(" ", end='')
        print(" ")



PrintStar(20)
PrintNums(10)
