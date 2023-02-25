def to_camel_case(text):

    text = str(text)
    ''' 
        the if statement will still run as long as the return value of find() is truthy 
        (i.e., not 0, None, [], {}, "", False). means if there is no _ or -, still it will run.
        because the return value of find() will be not 0.

        so we specify != -1, means if there's no accurance of the _ or - the elif will run.
    '''
    if text.find('_') or text.find('-') != -1:
        new_text = text.replace('_', ' ').replace('-', ' ') 
        split_text = new_text.split(' ') # split will create a list ['the', 'brown', 'fox']
        camel = ''
        camel += split_text[0]
        for words in split_text[1:]:
            camel += words.capitalize()
        print(camel)

    elif text == '':
        print('') 
    
    else:
        print('Invalid')
                
text= 'the_stealth-warrior'
to_camel_case(text)

        
        

            




