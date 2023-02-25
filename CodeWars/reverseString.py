'''
    spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw" 
    spinWords( "This is a test") => returns "This is a test" 
    spinWords( "This is another test" )=> returns "This is rehtona test
'''

def spin_words(sentence):
    sentence = str(sentence) 
    #spliting the string ex. ['Hey', 'fellow', 'warriors']
    new_sentence = sentence.split()
    print(new_sentence)

    '''
        we are taking the indexs of the new_string(list) in i and spliting them into
        new lists ['Hey'], ['fellow'], ['warriors']. and appending them into another list
        new_list = [['Hey'], ['fellow'], ['warriors']].
    '''

    new_list = []
    for i in range(len(new_sentence)):
        inner_new_sentence = new_sentence[i].split() # [['Hey'], ['fellow'], ['warriors']]
        new_list.append(inner_new_sentence)
    
    '''
        here we are creating a for loop where we are passing the new_list to
        inner_list ex. new_list = [['Hey'], ['fellow'], ['warriors']], first element
        ['hey'] will come to the inner list first, then that will pass to another
        for loop word.

        now word has ['hey']. now we are counting the length of the word, in our case
        ['hey'] which is 3. storing that number in count. 
        
        if the count is less then 5
        we are going to pass that word in les_5 and appending that word in to a new
        list name counts.

        if the count is >= 5 we are going to reverse that word and appending that word
        into counts, which is in case we are doing for the word ['fellow'] count = 6 
    
        al last joining the entire counts into one string or it will look like
        ['Hey', 'wollef', 'sroirraw'] after joining 'Hey wollef sroirraw'
    '''

    counts_word = []
    for inner_list in new_list:
        for word in inner_list:
            count = len(word)
            if count >= 5:
                new_word = word[::-1]

                
                counts_word.append(new_word)
            if count < 5:
                les_5 = word
                counts_word.append(les_5)

    # print(counts)
    final = ' '.join(counts_word)
    print(final)


words = 'Hey fellow warriors'
spin_words(words)