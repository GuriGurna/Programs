people = 30
cars = 40
trucks = 15 

if cars > people:
    print("we should take the cars.")

elif cars < people:
    print("we should not take the cars.")

else: 
    print("we can't decide ")

if trucks >cars:     
    print("maybe we could take the trucks. ")

elif trucks < cars:
    print("maybe we could take the trucks.")

else:
    print("we still cant't decide.")

if people > trucks:
    print("älright, lets just take the trucks" )
else:
    print("fine, let's stay home then")
