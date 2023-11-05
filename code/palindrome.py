def is_palindrome(num):
    num_str = str(num)
    if num_str == num_str[::-1]:
        return True 
    else:
        False

number = 12321
print(is_palindrome(number))