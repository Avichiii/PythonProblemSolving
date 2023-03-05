'[5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]'

def sort_array(source_array):
    sort_odd_array = []
    for i in source_array:
        if i % 2 != 0:
            sort_odd_array.append(i)       
    sort_odd_array.sort()
    for index, lst_value in enumerate(source_array):
        if lst_value % 2 != 0:
            # Poping the 0th index of sort_arr and replacing it with source's odd index
            source_array[index] = sort_odd_array.pop(0)
    return source_array
        
print(sort_array([5, 8, 6, 3, 4]))