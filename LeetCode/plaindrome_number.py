def isPalindrome(integer_plaindrome):
    if integer_plaindrome in range(1,9+1):
        return True
    
    integer_plaindrome = '-'.join(str(integer_plaindrome)).split('-')
    # testing if the first and last characters are same
    if integer_plaindrome[0] == integer_plaindrome[-1]:
        # [::-1] so we can reverse it and compare it with left side
        if integer_plaindrome[1:] == integer_plaindrome[:-1][::-1]:
            return True
        else:
            return False



print(isPalindrome(541323145))


# Was Trying Different Things with Statistics Moudel's median 
'''
    median_number = median(list(map(int, integer_plaindrome)))

    # median_number = str(median_number)
    print(integer_plaindrome)
    print(median_number)
    range_number = 0
    for i, values in enumerate(integer_plaindrome):
        if median_number == values:
            range_number += i
    #print(integer_plaindrome[0:range_number+1], integer_plaindrome[range_number:][::-1])
'''

