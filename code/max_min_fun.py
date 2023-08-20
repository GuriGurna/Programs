
def maxnum(list):
    largest= (0)
    for i in list:
        if i > largest:
            largest=i 
    print(largest)        


def minnum(list):
    smallest=(999999999999999999999)
    for i in list:
        if i < smallest:
            smallest=i
    print(smallest) 

list = [1, 2, 3, 4, 5,]
maxnum(list)
minnum(list)
