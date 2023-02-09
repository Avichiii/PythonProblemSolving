'''
    find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
    find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55

'''

def find_unique(arr):

    unique = []

    for i in arr:
        if arr.count(i) != 1:
            pass
        else:
            unique.append(i)

        
    for i in unique:
        print(i)

 



def find_uniq(arr):
    new_arr = set(arr) 
    print(new_arr) #{1, 5.02}
    for i in new_arr:
        # we are saying if the i {1 or 5.0} occurrence is 1 in the arr.
        # 1 is more then once present in the arr so it will be neglected 
        if arr.count(i) == 1:
            print(i)
find_uniq([ 1, 1, 1, 5.02,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1, 1, 1 ])
            