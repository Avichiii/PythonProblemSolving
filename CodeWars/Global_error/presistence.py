# Using Global variable
counter = 0

def mul(n):
    global counter
    n = str(n)
    multiplier_ = 1
    counter += 1
    for i in n[0:]:
        multiplier_ *= int(i)
    return multiplier_

def persistence(n):
    global counter
    with open('persistence.txt', 'a') as f:
        f.write(f'integer: {n}\n')
    n=str(n)
    if len(n) == 1:
        return counter
    multiplier= mul(n)
    if len(str(multiplier)) > 1:
        return persistence(multiplier)
    elif len(str(multiplier)) == 1:
        with open('persistence.txt', 'a') as f:
            f.write(f'value: {multiplier}, count: {counter}\n')

for index in range(11,1111):
    persistence(index)



