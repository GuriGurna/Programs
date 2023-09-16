'''.
Write the function subStringMatchExact.This function takes two arguments: a target string,
and a key string. It should return a tuple of the starting points of matches of the key string in the target
string, when indexing starts at 0. Complete the definition for
def subStringMatchExact(target,key):
For example,
subStringMatchExact("atgacatgcacaagtatgcat","atgc")
would return the tuple (5, 15). The file ps3_template.py includes some test strings that you can use to
test your function. In particular, we provide two target strings:
target1 = 'atgacatgcacaagtatgcat'
target2 = 'atgaatgcatggatgtaaatgcag'
and four key strings:
key10 = 'a'
key11 = 'atg'
key12 = 'atgc'
key13 = 'atgca'
Test your function on each combination of key and target string, as well as other examples that you '''

def subStringMatchExact(target,key):
    starting_points = []
    for i in range(len(target) - len(key) + 1 ):
        if target[i:i + len(key)] == key:
            starting_points.append(i)
    return starting_points        

target = "atgacatgcacaagtatgcat"
key = "atgc"
print(subStringMatchExact(target,key))            