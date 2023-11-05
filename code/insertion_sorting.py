def bubble_sorting(arr):
    for i in range(1 ,len(arr)):
        x = i 
        while x > 0 and arr[x] < arr[x-1]:
            a = arr[x-1]
            arr[x-1] = arr[x]
            arr[x] = a 
            x = x - 1
    return arr

array = [1,4,7,9,8,2,6,3,5]
print(bubble_sorting(array))