'''
    " Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"
    "    Hello     World   "                  =>  "#HelloWorld"
    ""                                        =>  false
'''

def generate_hashtag(s):
    s = str(s)
    lst_ = s.split()

    result = '#'  + ''
    for i in lst_:
        result += i.capitalize()
    
    # print(result)
    count = len(result)
    if count >  140:
        print(False)

        '''
            # we mention 1 because # in to the result taking 1 space
            # in that case even if the input is empty it will give # so we are specifying > 1
            # so it can count the numbers excluding the #
        '''     
    elif count < 140 and count > 1:
        print(result)
    elif s == '':
        print(False)


generate_hashtag(" Hello there thanks for trying my Kata")