def mean(x):
    length = len(x)
    sum = 0
    for j in range(length):
        sum = sum+x[j]
    x_mean = sum/length
    return x_mean

x = [101,323,121,412,236,478,355]

print(mean(x))

