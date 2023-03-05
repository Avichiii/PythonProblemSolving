'[20,37,20,21], 1 ------>  [20,37,21]'

def delete_nth(order,max_e):
    nth_lst = []
    #Reversing the order
    order = order[::-1]
    for values in order:
        nth_lst.append(values)
        if nth_lst.count(values) > max_e:
            # Remove number from the start of the list # 
            # in this case it's actully removing from the end because we are using [::-1] 
            nth_lst.remove(values)
            
    # reversing the list back to the original order
    return nth_lst[::-1]

print(delete_nth([1,2,3,1,2,1,2,3], 2))

'''
    [1, 2, 3, 1, 1, 2, 1, 2, 3, 3, 2, 4, 5, 3]
    [1, 2, 3, 1, 1, 2, 2, 3, 3, 4, 5]
'''