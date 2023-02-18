'''
    trim("Creating kata is fun", 14) should return "Creating ka..."
'''
'''
string > size = ...
'''
def trim(phrase, size):
    phrase = str(phrase)
    
    if len(phrase) <= size:
        return phrase
    elif size <=3 :
        return phrase[:size] + '...'
    else:
        return phrase[:size-3] + '...'

print(trim("Creating kata is fun", 14))
