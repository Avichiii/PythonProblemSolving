

def is_pangram(string):
    string = str(string)
    string = string.lower()
    
    
    all_letters = 'abcdefghijklmnopqrstuvwxyz'

    missing = ''
    for letter in all_letters:
        if letter not in string:
            missing += letter
    
    if len(missing) != 0:
        print('missing:' + missing)
    else:
        print('paragram')


s = 'The quick brown fox jumps over the lazy dog.'
is_pangram(s)
