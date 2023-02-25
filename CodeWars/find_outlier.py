def find_outlier(integers):
    even = []
    odd = []
    other = []
    for i in integers:
        if i % 2 != 0:
            odd.append(i)
        elif i % 3 != 0:
            even.append(i)
        else:
            other.append(i)

    if len(even) >= len(odd) and odd != []:
        return odd[0]
    elif len(even) <= len(odd) and even != []:
        return even[0]
    elif len(even) == 0 and len(odd) >= 1:
        return odd[0]
    else:
        return other[0]
    
print(find_outlier([0, 1, 2]))