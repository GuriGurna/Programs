n= 10
count = 0 
answer=[]
for i in range(1,n+1):
    for j in range(2,n+1):
        if i%j == 0:
            count+=1
    if count == 1:        
        answer.append(i)
    count=0
print(answer)