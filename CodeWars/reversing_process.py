import string

def own_aschii(char):
    aschii = {}
    for key, value in enumerate(string.ascii_lowercase):
        aschii[value] = key

    if isinstance(char, str):
        for key in aschii.keys():
            if key == char:
                return aschii[key] # 1,2 etc...
            
    elif isinstance(char, list):
        final_string = ''
        for number in char:
            for key, values in aschii.items():
                if values == number:
                    final_string += key # a, b etc...
        
        return final_string 
    
def decode(r:str):
    number = ''
    string = []
    for num in r:
        if num.isdigit() == True:
            number += num
        else:
            # converts char to the corresponding number
            char_num = own_aschii(num)
            string.append(char_num)

    final_charecter_numbers = []
    for index in range(len(string)):
        for original in range(0, 25+1):
            # this is the formula: original * (numberUsed for decodeing) % 26 = (number of the encoded char)
            if original * int(number) % 26 == string[index]:
                final_charecter_numbers.append(original)
    
    # incase len of the chars not equal: afe == akeaoaojti ( this will happen if the encoding is wrong )
    if len(string) != len(final_charecter_numbers):
        return 'Impossible to decode'
    
    decoded_string = own_aschii(final_charecter_numbers)
    
    return decoded_string
    

print(decode("5057aan"))
# print(own_aschii('e'))