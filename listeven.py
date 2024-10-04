num = int(input(" Enter the length : "))
list1 = []
for i in range(0,num):
    ele = int(input())
    list1.append(ele) #i=0 #ele 65  #list1 = 65

print(list1)

even1 = []
for i in list1:
    if(i%2 == 0):
        even1.append(i)

print(even1)