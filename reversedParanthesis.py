'''
    solve(")(") = 2 Because we need to reverse ")" to "(" and "(" to ")". These are 2 reversals. 
    solve("(((())") = 1 We need to reverse just one "(" parenthesis to make it balanced.
    solve("(((") = -1 Not possible to form balanced parenthesis. Return -1.
'''

def valid_word(seq, word): 
    #     seq ['code', 'wars','star']
    #     word 'codewars'

    
    self_seq = ''.join(seq)
    seq_lis_ = []
    word_lis_ = []

    for i in self_seq:
        seq_lis_.append(i)
    # print(seq_lis_)

    for j in word:
        word_lis_.append(j)
    # print(word_lis_)

    new_i = []
    for i in seq_lis_:
        if i in word_lis_:
           new_i += i
    
    # word_lis_ = ''.join(word_lis_)
    # new_i = ''.join(new_i)

    if seq == []:
        print(False)
    elif new_i == word_lis_:
        print(True)
    elif new_i != word_lis_:
        print(False)

    print(new_i)
    print(word_lis_)

    


s  = ['psnjp', 'y', 'groql', 'ibkg', 'cg', 'vk', 'lf', 'oghsw', 'ee', 'usr', 'dx']
w = 'w'
['code', 'wars']
valid_word(s, w)

exit()
def solve(s):
    s = str(s)
    
    open_per = 0
    close_per = 0
    for count in s:
        if count == '(':
            open_per += 1
        elif count == ')':
            close_per += 1

    lis_ = []
    for i in s:
        lis_.append(i)
    
    
    for i in lis_[0:]:
        if i == '(' or i ==')':     
            pass

s = '())()))))()()('
solve(s)

