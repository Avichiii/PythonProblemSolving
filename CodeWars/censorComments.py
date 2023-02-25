def disemvowel(string_):
    string_ = str(string_)
    string = ''

    if string_ == 'a' or 'e' or 'i' or 'o' or 'u' or 'A' or 'E' or 'I' or 'O' or 'U':
        string += string_.replace('a', '').replace('e', '').replace('i', '').replace('o', '').replace('u','').replace('A', '').replace('E', '').replace('I', '').replace('O', '').replace('U','')

    print(string)


st = "This website is for losers LOL!"
disemvowel(st)