def array_diff(array_a, array_b):
    if array_b == []:
        return array_a
    elif array_a == []:
        return [] 
    
    result = []
    for i in array_a:
        if i not in array_b:
            result.append(i)
    return result

print(array_diff([8, -17, 5, 18, 3, -9], [10, -12, 19, 16]))