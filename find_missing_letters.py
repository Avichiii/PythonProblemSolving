def find_missing_letter(chars):
    s = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    match = False
    count = 0
    for letter in s:
        if letter == chars[count]:
            match = True
            count = count +1
        elif match == True:
            print(letter)

        '''
             This is to check count doesn't exceed len of chars or in this case 4
             Or we will IndexError: list index out of range
        '''
        if count >= len(chars):
            break

find_missing_letter(['O','Q','R','S','U'])


'''
    the loop will go through each letter. a-N letters it will be skipped.
    (first letter will have a; a will be matched with chars[0] th index; if it's false
    which it is because chars[0] is O; it will move to elif, that will be false
    becase match is set to False, like this the loop will go on..)

    when it will come to O the if will be true and match = True will set and
    count = 1 will set

    after that letter will be P and chars[1]; in this case chars[1] will be Q not P

    so elif will run and it will because match was set to True and P will return


    we have the match = False flag; so we can start counting from where the chars
    list is starting.
'''
