'''
    "abcde" -> 0 # no characters repeats more than once
    "aabbcde" -> 2 # 'a' and 'b'
    "aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
    "indivisibility" -> 1 # 'i' occurs six times
    "Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
    "aA11" -> 2 # 'a' and '1'
    "ABBA" -> 2 # 'A' and 'B' each occur twice
'''

def duplicate_count(text):
    text = str(text)

    if text == '':
        print(0)
    '''Lowercase the text string so it will be esier to 
    count the duplicates'''
    text_low = text.lower()
    count = 0

    # Set so we can store the unique values
    processed = set()
    
    for i in text:
        '''if the count of the letter is more then 1
        and that charater is not in the set it will
        enter the loop and count will increment'''
        if text_low.count(i) > 1 and i not in processed:
            processed.add(i.lower())
            count += 1

    print(processed)
    print(count)

duplicate_count("aabBcde")