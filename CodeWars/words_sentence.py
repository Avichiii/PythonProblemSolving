'''
    ['ninja', 'samurai', 'ronin'] --> "ninja, samurai and ronin"
    ['ninja', '', 'ronin'] --> "ninja and ronin"
    [] -->""
'''
#has bugs
def format_words(words):
    
    # Return '' if the list is empty
    if words == []:return ''
    elif words == None:return ''
    elif words == ['']:return ''

    # Removes the '' from the list if there's any
    new_words = []
    for i in words:
        if i == '':
            pass
        else:
            new_words.append(i)
    
    # Format the list
    result = ''
    if len(new_words) == 1:
        string_ = ''
        for i in new_words:
            string_ += i
        # spliting the list items if there's a string in the list containing only one '' wraping the indexes
        '''['abcdefghijklmnopqrstuv, abcdefghijklmnop'] '''
        split = string_.replace(',', '').split(' ')
        # print(split)
        if len(split) > 1:
            for i in split:
                if i == split[-1]:
                    result += f'and {i}'
                elif i == split[-2]:
                    result += f'{i} '
                else:
                    result += f'{i}, '
        else:
            return new_words[0]

    elif len(new_words) > 1:
        for i in new_words:
            if i == new_words[-1]:
                result += f'and {i}'
            elif i == new_words[-2]:
                result += f'{i} '
            else:
                result += f'{i}, '

    return result


print(format_words(['abcdefghijklmn, abcdefg, abcdefghijk, abcdefghijklmnopqrstuvwx abcdefghijklmnop, abcdefghijklmnopqrstuvwx abcdefgh']))

['abcdefghijklmnop, abcd and abcdefghijklmnop']
['ninja', 'samurai', 'ronin', 'zoro', 'avichii', 'paste']


'''
            'abcdefghijklmn, abcdefg, abcdefghijk, abcdefghijklmnopqrstuvwx abcdefghijklmnop, abcdefghijklmnopqrstuvwx and abcdefgh' 
should equal 
            'abcdefghijklmn, abcdefg, abcdefghijk, abcdefghijklmnopqrstuvwx, abcdefghijklmnop, abcdefghijklmnopqrstuvwx and abcdefgh'
'''


# No bugs
def format_words(words):
    if words == []:return ''
    elif words == None:return ''
    elif words == ['']:return ''

    new_words = []
    for i in words:
        if i == '':
            pass
        else:
            new_words.append(i)
    
    result = ''
    if len(new_words) == 1:
        string_ = ''
        for i in new_words:
            string_ += i
        split = string_.replace(',', '').split(' ')
        
        if len(split) > 1:
            for i in range(len(split)):
                if i == len(split) - 1:
                    result += f'and {split[i]}'
                elif i == len(split) - 2:
                    result += f'{split[i]} '
                else:
                    result += f'{split[i]}, '
        else:
            return new_words[0]

    elif len(new_words) > 1:
        for i in range(len(new_words)):
            if i == len(new_words) - 1:
                result += f'and {new_words[i]}'
            elif i == len(new_words) - 2:
                result += f'{new_words[i]} '
            else:
                result += f'{new_words[i]}, '

    return result
print(format_words(['abcdefghijklmn, abcdefg, abcdefghijk, abcdefghijklmnopqrstuvwx abcdefghijklmnop, abcdefghijklmnopqrstuvwx abcdefgh']))