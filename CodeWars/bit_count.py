def count_bits(n):
    bin_a = bin(n)
    count = bin_a.count('1') 
    return count

count_bits(1234)