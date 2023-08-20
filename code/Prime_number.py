"""# Create a function named is_prime which takes a number as an argument and return a boolean indicating whether the given number is prime or not.

Example:

    > is_prime(2)
    > True
    
    > is_prime(3)
    > True
    
    > is_prime(4)
    > False
    
    > is_prime(31)
    > True """


def is_prime(x):
    if x==1:
        return True
    for i in range(2,x):
        if x%i==0:
            return False
    
    else: return True
    
print(is_prime(7)) 