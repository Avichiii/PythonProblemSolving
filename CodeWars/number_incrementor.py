'''
    foo -> foo1
    foobar23 -> foobar24
    foo0042 -> foo0043
    foo9 -> foo10
    foo099 -> foo100
'''



def increment_string(strng):
    strng = str(strng)

    # strip the decimals from the right
    only_strings = strng.rstrip('0123456789')

    # get the part of strng that was stripped #in this case 01
    ints = strng[len(only_strings):]


    if len(ints) == 0:
        return strng + '1'

    else:
       # find the length of ints # in this case it's 2; 01
       length = len(ints)
    
       # add 1 to ints in this case 01 + 1 = 2
       new_ints = int(ints) + 1

       # pad new_ints with zeroes on the left #it will add 0 before 2
       new_ints = str(new_ints).zfill(length)

       return only_strings + new_ints



    

    
print(increment_string('foo01000012'))
