#Not My Algo
def find_even_index(lst):
    left_sum = 0
    right_sum = sum(lst)
    for i, lst_values in enumerate(lst):
        right_sum -= lst_values
        if left_sum == right_sum:
            return i
        left_sum += lst_values
    return -1

print(find_even_index([1,2,3,4,3,2,1]))