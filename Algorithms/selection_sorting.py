def selecting_sorting(Arr):
    for i in range(0 ,len(Arr)-1):
        for j in range(i+1 ,len(Arr)):
            if Arr[i] > Arr[j]:
                a = Arr[i]
                Arr[i] = Arr[j]
                Arr[j] = a 
    return Arr         
                
array = [4,6,5,8,9,54,34,45,67]                
print(selecting_sorting(array))             