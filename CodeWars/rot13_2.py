import string
punctuation = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
def rot13(message):
    ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
    rot13_message = ''
    for rot in range(len(message)):
        if message[rot] in ascii_lowercase:
            index = ascii_lowercase.index(message[rot])
            rot13_message += ascii_lowercase[(index+13)%26]
        elif message[rot] in ascii_lowercase.upper():
            index = ascii_lowercase.upper().index(message[rot])
            rot13_message += ascii_lowercase.upper()[(index+13)%26]
        else:
            rot13_message += message[rot]
    print(rot13_message)
rot13("Guvf vf npghnyyl gur svefg xngn V rire znqr. Gunaxf sbe svavfuvat vg! :)")