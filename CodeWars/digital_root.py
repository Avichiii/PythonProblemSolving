
def summing(num):
    num = str(num)
    sum_ = 0
    for i in num[0:]:
        sum_ += int(i)
    return sum_

def digital_root(n):
    n = str(n)
    sum_ = summing(n)
    if len(str(sum_)) > 1:
        return digital_root(sum_)
    elif len(str(sum_)) == 1:
        return sum_
    
print(digital_root(999))


