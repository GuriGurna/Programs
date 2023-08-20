"""# Create a funtion named p_range which takes 2 numbers as argument and return a list of all prime numbers between those 2 numbers. If only one 
argument is provided assume first number to be 0 and consider given argument as second number of the range. Make sure to use is_prime function you
 created in previous exercise.

Example

    > p_range(3, 10)
    > [3, 5, 7]
    
    > p_range(10)
    > [2, 3, 5, 7]"""

from Prime_number import is_prime

list=[]
def prime_range(a,b):
    for i in range(a,b+1):
        if is_prime(i):
            list.append(i)
    print(list)

prime_range(1,1000)
