def narcissistic( value ):
    value = str(value)
    power = len(value)
    armstrong = 0
    for i in value:
        armstrong += int(i)**power
    if armstrong == int(value):
        return True
    else:
        return False

print(narcissistic(153))