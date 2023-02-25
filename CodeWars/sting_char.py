def first_non_repeating_letter(string):
    string = str(string)

    s = string.lower()

    for letter in string:
        if s.count(letter.lower()) == 1:
            return letter
    
    return ''

print(first_non_repeating_letter('stresssssss'))