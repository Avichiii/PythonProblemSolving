'''
    move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]
'''


def move_zeros(lst):
    lst = list(lst)
    new_lst = []
    zero_lst = []
    for i in lst:
        if i != 0:
            new_lst.append(i)
        else:
            zero_lst.append(i)
    
    final_lst = new_lst + zero_lst
    print(final_lst)


move_zeros([1, 0, 0, 1, 2, 0, 0, 0, 0, 0, 1, 3])