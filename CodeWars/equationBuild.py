import math
from string import ascii_lowercase
'''
quadratic_builder("(x+2)(x+3)")  #return "x^2+5x+6"
quadratic_builder("(x-2)(x+7)")  #return "x^2+5x-14"
quadratic_builder("(3y+2)(y+5)")  #return "3y^2+17y+10"
quadratic_builder("(-h-7)(4h+3)")  #return "-4h^2-31h-21"

'''

def quadratic_builder(expression:str):
    ex = expression.split(')') 
    val = [] # ex ['-h-7', '4h+3']
    for e in ex:
        if e != '':
            val.append(e[1:])

    newVal = []
    signCharacter = '' # x, a, b
    sign = [] # +, -
    for word in val:
        for letter in word:
            if letter == '+' or letter == '-':
                sign.append(letter)
            if letter in ascii_lowercase:
                if len(signCharacter) < 1:
                    signCharacter += letter
                newVal.append(word.replace(letter, ''))
       


quadratic_builder("(-h-7)(4h+3)")
