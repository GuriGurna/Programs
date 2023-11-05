def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here'
    list1=[]
    list2=[]
    
    for i in apples:
        distance_apple = i + a 
        if distance_apple>=s:
            list1.append(distance_apple)
        
    for j in oranges :
        distance_oranges = j + b 
        if distance_oranges<=t:
            list2.append(distance_oranges)
    
    no_of_apples=len(list1)
    no_of_oranges=len(list2)
            
    print(no_of_apples) 
    print(no_of_oranges) 


s=7 
t= 11
a =5 
b=15
m=3
n=2
apples = [-2 ,2, 1]
oranges = [5 ,-6] 
countApplesAndOranges(s, t, a, b, apples, oranges)