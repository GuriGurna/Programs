'''Write a function, called which takes two arguments: a target
string and a key string. This function should return a tuple of all starting points of matches of the key to
the target, such that at exactly one element of the key is incorrectly matched to the target. Complete the
definition
Save your answers in a file named ps3d.py.
subStringMatchExactlyOneSub
def subStringMatchExactlyOneSub(target,key):'''

def subStringMatchExactlyOneSub(target,key):
    matches = []

    for i in range(len(target) - len(key) + 1):
        do_not_match = 0 
        
        for j in range(len(key)):
            
            if target[i+j] != key[j]:
                do_not_match += 1
           
            if do_not_match > 1 :
                break
       
        if do_not_match == 1 :
            matches.append(i)
    
    return matches


target = "abcaabcdabddahbadjdngaccd"
key = "abcd"
print(subStringMatchExactlyOneSub(target,key))
