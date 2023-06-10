list1 = ["hello" , 1 , 34 , 78 , "guri" ]

list2 = list1.copy()

list3 = list1[:]

list4 = list(list1)

list5 = []

for i in range(len(list1)):
    a= list1[i]

    list5.append(a)

list6 = list1

# list2[3] = 50
# list6[3] = 50
list1[3] = 50

print(list1)
print(list2)
print(list3)
print(list4)
print(list5)
print(list6)