def camel_case(string):
    string = str(string).split(' ')
    camel_str = ''
    for i in string:
        camel_str += i.capitalize()
    return camel_str

print(camel_case('hello world'))