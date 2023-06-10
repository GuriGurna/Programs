totals = [50, 51, 52, 53, 54, 55]
def combinations(total):
    list = []
    
    for a in range(total // 6 + 1):
        for b in range(total // 9 + 1):
            for c in range(total // 20 + 1):
                if (6 * a + 9 * b + 20 * c) == total:
                    list.append((a, b, c))
    print(list)
    return list
    
for x in totals:
    list = combinations(x)
    print(f"Combinations for {x} McNuggets:")
    for n in list:
        print(f"6-pack x {n[0]}, 9-pack x {n[1]}, 20-pack x {n[2]}")
    print("--------------------------------------")
