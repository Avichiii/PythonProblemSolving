def pig_it(text):
    punctuation = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
    text = str(text).split()
    mod_str = []
    for iter in text:
        if iter not in punctuation:
            replaced_first_char = iter[1:]
            new_iter = replaced_first_char + iter[0] + 'ay'
            mod_str.append(new_iter)
        else:
            mod_str.append(iter)
    return ' '.join(mod_str)

print(pig_it("Hello world !"))

'''
    'ucullusCay onnay acitfay onachummay' should equal 
    'ucullusCay onnay acitfay onachummay'
'''