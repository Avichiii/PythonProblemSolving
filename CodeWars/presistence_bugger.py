counter = 0

def mul(n, counter):
    # global counter
    n = str(n)
    multiplier_ = 1
    # counter += 1
    for i in n[0:]:
        multiplier_ *= int(i)
    return multiplier_,counter+1

def persistence(n, counter= 0):
    # global counter
    n=str(n)
    if len(n) == 1:
        return counter
    multiplier, counter = mul(n, counter)
    if len(str(multiplier)) > 1:
        return persistence(multiplier,counter)
    elif len(str(multiplier)) == 1:
        return counter
    
print(persistence(419))