
def rot13(message):
    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    rot13_message = ''

    for i in range(len(message)):
        '''
        The rasone we % 26 to set the index from 0 after compliting 26th alphabet
        '''
        if message[i] in lowercase:
            index = lowercase.index(message[i])
            rot13_message += lowercase[(index+13)%26]
        elif message[i] in lowercase.upper():
            index = lowercase.upper().index(message[i])
            rot13_message += lowercase.upper()[(index+13)%26] 
        else:
            rot13_message += message[i]
    return rot13_message


print(rot13('DIAMOND'))
