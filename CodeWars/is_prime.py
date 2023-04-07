import math
def is_prime(num):
    if num <= 1:
        return False
    count = 0
    for i in range(1,int(math.sqrt(num)+1)):
        if num % i == 0:
            count += 1
    if count > 1:
        return False
    return True


print(is_prime(7))

'''
If we loop through all numbers up to the square root of num 
without finding a divisor, then num is a prime number and we 
can return True.
'''