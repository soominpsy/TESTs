#--coding: UTF-8--
from __future__ import print_function  # this is use for priting without change line

def PrintStar(n):                      # 별표 피라미드를 만드는 함수 입니다. 
    for i in range(n):                    # i,j parameter would be used for iterate in column and row for each 
        temp1 = n-i-1                      # "temp1" representing the first position of * should be printed for each row 
        temp2 = n+i-1                      # "temp2" representing the first position of * should be printed for each row 
        for j in range(2*n-1):               
            if(i==0):                   # for the first line 
                if(j==temp1):
                    print("*", end='')   # printing "*" without change line
                else:
                    print(" ", end='')   # printing " " without change line
            else :
                if(temp1==j & temp1<=temp2):  
                    print("*", end='')
                    temp1 = temp1+2            # make a empty space between printing stars
                else: 
                    print(" ", end='')
        print(" ")

def PrintNums(n):                  # this is similar with PrintStar() function 
    for i in range(n):
        temp1 = n-i-1
        temp2 = n+i-1
        kk = 1                    # define kk for printing numbers
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
