'''lem 1.
Write two functions, called countSubStringMatch and countSubStringMatchRecursive that
take two arguments, a key string and a target string. These functions iteratively and recursively count
the number of instances of the key in the target string. You should complete definitions for
def countSubStringMatch(target,key):
and
def countSubStringMatchRecursive (target, key):'''

def countsubstringmatch(target,key):
    count = 0
    len_key = len(key)
    
    for i in range(len(target) - len_key + 1):
        if target[i:i + len_key] == key:
            count +=1
    return count    
      

def countsubstringmatchrecursive(target,key):
    if len(target) < len(key):
        return 0
    
    len_key = len(key)
    
    if target[:len_key] == key:
        return 1 + countsubstringmatchrecursive(target[1:],key)
    
    else :
        return countsubstringmatchrecursive(target[1:],key)

target_string = "atgacatgcacaagtatgcat"
key_string = "atgc"
print("iterative ", countsubstringmatch(target_string,key_string))
print("recurcive",countsubstringmatchrecursive(target_string,key_string))    