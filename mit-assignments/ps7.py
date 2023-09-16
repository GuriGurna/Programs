'''This problem set is designed to help you solidify your understanding of some
material that we have covered in lecture, but not emphasized on the programming
problems. You should do it, but do NOT hand it in.

1) What is the computational complexity of fact0? Explain your answer.
def fact0(i):
assert type(i) == int and i >= 0
if i == 0 or i == 1:
return 1
return i * fact0(i-1)


ans = o(i) or 0(n) because each time recursion uses i-1 to reach end case  linear 

2) What is the computational complexity of fact1? Explain your answer.
def fact1(i):
assert type(i) == int and i >= 0
res = 1
while i > 1:
res = res * i
i -= 1
return res

ans = 0(i) or 0(n) linear because every tiem i runs through loop 

3) What is the computational complexity of makeSet? Explain your answer.
def makeSet(s):
assert type(s) == str
res = ''
for c in s:
if not c in res:
res = res + c
return res

ans = 0(n^2) because two loops will run one for letters in string and secods to find letter in result string 

4) What is the computational complexity of intersect? Explain your answer.
def intersect(s1, s2):
assert type(s1) == str and type(s2) == str
s1 = makeSet(s1)
s2 = makeSet(s2)
res = ''
for e in s1:
if e in s2:
res = res + e
return res

ans = 0(n^2) because one loop willrun and scond will mstch the leeters in another string 

5) Present a hand simulation of the code below. Describe the value to which each
identifier is bound after each step of the computation. Note that “s1” and “s2” exist
in more than one scope.
def swap0(s1, s2):
assert type(s1) == list and type(s2) == list
tmp = s1[:]
s1 = s2[:]
s2 = tmp
return
s1 = [1]
s2 = [2]
swap0(s1, s2)
print s1, s2

ans = first it takes two lists as an argument 
    then tmp got assigned to list s1 which is 1
    them s1 got assigned to list s2 which is 2 
    then s2 becomes tmp which is 1
    which is s1 contains 2 and s2 contains 1  

    but fuction will only prints argumets taken by it 
    so function prints 1,2

6) Present a hand simulation of the following code:
def swap1(s1, s2):
assert type(s1) == list and type(s2) == list
return s2, s1
s1 = [1]
s2 = [2]
s1, s2 = swap1(s1, s2)
print s1, s2

ans = there are two list s s1 and s2
    first it return both the lists as values 2 and 1 
    and it runs s1 and s2 takes values as 2 and 1 respectively 
    and it prints 2 and 1 



7) Present a hand simulation of the following code:
def rev(s):
assert type(s) == list
for i in range(len(s)/2):
tmp = s[i]
s[i] = s[-(i+1)]
s[-(i+1)] = tmp
s = [1,2,3]
rev(s)
print s

ans = there is a list s 
     then we run a loop which takes half the lenghth of list 
     for i = 0 s[0] is 1 
     tmp becomes 1 
     then s[i] is assigned to s[-1] which becomes [3,2,1]
     which is futher assinged to tmp 

'''

