def duplicate_encode(word):
    word = str(word).lower()
    encode = []
    for i in word:
        if word.count(i) > 1:
            encode.append(')')
        else:
            encode.append('(')
    return ''.join(encode)

print(duplicate_encode('akcfwUvLGrrLdevyJzVM@ zKP'))
