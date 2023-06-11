def solve(arr:list):
    arr.reverse()
    newList = []
    for i in arr:
        if i not in newList:
            newList.append(i)
    newList.reverse()
    return newList


print(solve([3,4,4,3,6,3]))

