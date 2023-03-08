def romanToInt(roman_numer):
    roman = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    roman_numer = '-'.join(str(roman_numer)).split('-')

    unique = []
    for i in roman_numer:
        if i in roman.keys():
            unique.append(roman[i])

    checker = []
    sum_ = 0
    for j in unique:
        if j == 100 or j == 10 or j == 1:
            checker.append(j)

        if 100 in checker and (j == 1000 or j == 500):
            sum_ += j - 200

        elif 10 in checker and (j == 50 or j == 100):
            sum_ += j - 20

        elif 1 in checker and (j == 5 or j == 10):
            sum_ += j - 2

        else:
            sum_ += j

    return sum_


print(romanToInt("LVIII"))


'''       
        'II': 2,
        'III': 3,
        'IV': 4,

        'VI': 6,
        'VII': 7,
        'VIII': 8,
        'IX': 9,

        'XI': 11,
        'XII': 12,
        'XIII': 13,
        'XIV': 14,
        'XV': 15,
        'XVI': 16,
        'XVII': 17,
        'XVIII': 18,
        'XIX': 19,
        'XX': 20,
'''


