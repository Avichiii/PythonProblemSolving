def limit(number):
    if number < 0:
        return 0
    elif number > 255:
        return 255
    return number

def rgb(r, g, b):

    "{:02X}{:02X}{:02X}".format(limit(r), limit(g), limit(b))

print(rgb(5, 0, 0))


# def rgb(r, g, b):

#    hex_= f'{hex(r)[2:].upper()}{hex(g)[2:].upper()}{hex(b)[2:].upper()}'
#    print(hex_)


# rgb(255, 99, 71)

