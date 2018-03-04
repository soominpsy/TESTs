a = [101,323,121,412,236,478,355]
b=0
c=0
for i in a:
    b = b+i
    c = c+1    # (j) there is useful command called "len", which returns length of the list.
print(b/c)  


#from junho
b=0
for i in a:
    b = b+i
print(b/len(a))
