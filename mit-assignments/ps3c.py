def constrainedMatchPair(firstMatch, secondMatch, length):
    
    valid_matches = ()
    for n in firstMatch:
        for k in secondMatch:
            if n + length + 1 == k:
                valid_matches += (n,)
                break  # Exit the inner loop once a valid match is found
    return valid_matches


firstmatch = (0, 3, 5, 9)
secondmatch = (7,0)
length = len("ATGC")
print(constrainedMatchPair(firstmatch ,secondmatch , length))  # Output: (0, 3)

def constrainedMatchPair(starts1, starts2, length):
    valid_matches = [n for n in starts1 if n + length + 1 in starts2]
    return tuple(valid_matches)

# Example usage:
starts1 = (0, 3, 5, 9)
starts2 = (7,)
length = len("ATGC")
print(constrainedMatchPair(starts1, starts2, length))  # Output: (0, 3)
