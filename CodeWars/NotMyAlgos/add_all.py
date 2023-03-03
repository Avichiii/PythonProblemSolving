'([1,2,3]), 9)'
# Not my Algo
def add_all(lst):
    result = []
    while len(lst) > 1:
        lst.sort()
        firstTwoFromList = lst.pop(0) + lst.pop(0)
        lst.append(firstTwoFromList)
        result.append(firstTwoFromList)
    return sum(result)

print(add_all([1, 2, 3, 4, 5]))
