'[1,2,2,3,3,3,4,3,3,3,2,2,1] = 4'

def find_it(seq):
    if len(seq) == 1:
        return seq[0]
    set_ = set()
    for i in seq:
        '''
            this count the number of occurences of a int in a list and then 
            div the count with 2; if the reminder is not 0 then its a odd number.
        '''
        if seq.count(i) % 2 != 0:
            set_.add(i)
    for i in set_:
        return i
    

print(find_it([1,1,2,-2,5,2,4,4,-1,-2,5]))