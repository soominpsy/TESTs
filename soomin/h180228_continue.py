for i in range (10):
    if i==5:
        continue
    print(i,"continue")   # in this case, you print 10 times with i, what we probably not expected. please locate the "print" function inside of "else"

for i in range(10):
    if i==8:
        break   
    print(i,"break")      # in this case, you print 10 times with i, what we probably not expected. please locate the "print" function inside of "else"



# from junho
for i in range(10):
    if i ==5:
        continue
    elif i == 8 :
        break
    else:
        print(i)
    

