# Not my Algo
# This Function returns the elements
def sum_pairs(lst, s):
    cache = set()
    for i in lst:
        if s - i in cache:
            return [s - i, i]
        cache.add(i)

print(sum_pairs([2,7,11,15], 9))


