def high_and_low(numbers):
    numbers = list(map(int, str(numbers).split(" ")))
    min_n = min(numbers); max_n = max(numbers)
    return str(max_n) + " " + str(min_n)

print(high_and_low('8 3 -5 42 -1 0 0 -9 4 7 4 -4'))