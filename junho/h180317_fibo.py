


def fib(n):
    if n<=2 :
        return 1      # return 1  if place of number is 1 or 2
    else:
        return fib(n-1)+fib(n-2)  # if not, add nearest two numbers front of the number

for i in range(10):
    print(fib(i+1)," ", end='')

