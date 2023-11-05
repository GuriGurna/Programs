def bubble_sorting(Arr):
    for i in range(0 ,len(Arr)):
        for j in range(0 ,len(Arr)-1):
            if Arr[j] > Arr[j+1]:
                a = Arr[j]
                Arr[j] = Arr[j+1]
                Arr[j+1] = a 
    return Arr         
                
array = [1,9,6,7,8,3,5,4,2]                
print(bubble_sorting(array)) 