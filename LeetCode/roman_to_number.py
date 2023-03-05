def romanToInt(roman_numer):
    roman = {
        'I': 1,
        'II': 2,
        'III': 3,
        'IV': 4,
        'V': 5,
        'VI': 6,
        'VII': 7,
        'VIII': 8,
        'IX': 9,
        'X': 10,
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
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    roman_numer = '-'.join(str(roman_numer)).split('-')

    unique = []
    for i in roman_numer:
        if i == 'C' or i == 'X':
            unique.append(i)
        if i in roman.keys():
            print(roman[i] - 100)


romanToInt("CD")