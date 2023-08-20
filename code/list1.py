list = [121,323,2,435,6,7, 74 , 23 ,24,3,33,423,4,2,4,4,4,4,324,234,3]

for index , item in enumerate(list):
    if index % 2 == 0 and index <15:
        print(f"the {item} is at  {index +1 } number")