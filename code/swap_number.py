# Swap two elements in a list

# Testcases
# Input : List = [23, 65, 19, 90], pos1 = 1, pos2 = 3
# Output : [19, 65, 23, 90]

# Input : List = [1, 2, 3, 4, 5], pos1 = 2, pos2 = 5
# Output : [1, 5, 3, 4, 2]

def swapPositions(list, pos1, pos2):
    list[pos1 - 1], list[pos2 - 1] = list[pos2 - 1], list[pos1 - 1]

    return list

if __name__ == "__main__":
    print(swapPositions([23, 65, 19, 90], 1, 3))