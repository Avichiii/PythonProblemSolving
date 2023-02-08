'''
    pig_it('Pig latin is cool') # igPay atinlay siay oolcay
    pig_it('Hello world !')     # elloHay orldway !

'''

def pig_it(text):
    text = str(text)
    res = []

    for i in text.split():
        # if i is a alphabet character it will go into the loop
        if i.isalpha():
            res.append(i[1:] + i[0] + 'ayy')
        else:
            res.append(i)

    new_res = ' '.join(res)
    return new_res

print(pig_it('Pig latin is cool'))