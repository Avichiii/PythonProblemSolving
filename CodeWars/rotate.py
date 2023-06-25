def rotate(str_:str):
    rotateArray = []
    for i in range(len(str_)):
        crwd = str_[i+1:] + str_[:i+1]
        rotateArray.append(crwd)
    return rotateArray

print(rotate('Hello'))