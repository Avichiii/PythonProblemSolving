# Arithmatic Functions
add = lambda a1,a2: a1 + a2
sub = lambda a1,a2: a1 - a2 
div = lambda a1,a2: a1 // a2 
mul = lambda a1,a2: a1 * a2 
pow = lambda a1,a2: a1 ** a2

def zip_with(fn,a1,a2):
    result = []
    # Zipping a1 & a2 = (0,6) (1,5).... # only taking the shortest len list
    for i, j in zip(a1,a2):
        # calling the fn func and storing the output
        result.append(fn(i,j))
    return result

print(zip_with(add,[0,1,2,3,4,5], [6,5,4,3,2  ]))


