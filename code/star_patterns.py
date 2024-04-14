def full_star_pyramid(rows):
    for i in range(1, rows + 1):
        print(" " * (rows - i) + "*" * (2 * i - 1))

full_star_pyramid(5)


def Right_hand_pyramid(rows):
    for i in range(1, rows + 1):
        print('*' * i)

Right_hand_pyramid(5)


def Inverted_hand_pyramid(rows):
    for i in range(3,0 ,-1): 
        print('0' * 3)

Inverted_hand_pyramid(3)