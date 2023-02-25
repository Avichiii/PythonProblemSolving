def alphabet_position(text):
    # Char with Values
    dict_ = {}
    string_ = 'abcdefghijklmnopqrstuvwxyz'
    for index , char in enumerate(string_):
        dict_[char] = index + 1

    # Convert Text Chars to integers
    r_text = []
    for i in text.lower():
        if i in dict_.keys():
             r_text.append(str(dict_[i]))
    return ' '.join(r_text)

print(alphabet_position('hello guys'))