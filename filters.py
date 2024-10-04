def even(n):
    return n%2 == 0
num1 = [1,10,200,21,36,42]
evennumbers = filter(even,num1)
print(list(evennumbers))