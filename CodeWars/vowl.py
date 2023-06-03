def disemvowel(string_):
    l = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    n = ''
    for str in list(string_):
        for i in str:
            if i not in l:
                n+=i
    return n

print(disemvowel('hello'))