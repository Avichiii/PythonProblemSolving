from string import digits, ascii_letters, punctuation

def words_to_hex(words:str):
    newWords = ''
    constraint = str(digits + ascii_letters + punctuation + ' ')
    for i in words:
        if i in constraint:
            newWords += i
    splitedWords = newWords.split(' ')

    resultAschii = []
    for word in splitedWords:
        if len(word) > 3:
            counter = 0
            getAscii = []
            for char in word:
                if counter < 3:
                    getAscii.append(ord(char))
                    counter += 1
            resultAschii.append(getAscii)

        elif len(word) < 3:
            getAscii = []
            for char in word:
                getAscii.append(ord(char))
            while len(getAscii) != 3:
                getAscii.append(0)
            resultAschii.append(getAscii)

        else:
            getAscii = []
            for char in word:    
                getAscii.append(ord(char))
            resultAschii.append(getAscii)

    hexCode = []
    for rgb in resultAschii:
        hexCode.append('#{:02x}{:02x}{:02x}'.format(rgb[0], rgb[1], rgb[2]))

    return hexCode


print(words_to_hex('Hello, my name is Gary and I like cheese.'))
