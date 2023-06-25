from string import ascii_lowercase
def solve(s:str) -> int:
    checker = {}
    for index, letter in enumerate(ascii_lowercase):
        checker[letter] = index + 1
    
    result = []
    stack = []
    for i in s:
        if i not in ['a','e','i','o','u']:
            stack.append(checker[i])
        else:
            result.append(sum([i for i in stack]))
            stack = []
    
    # for last sub string
    if stack != []:
        result.append(sum([i for i in stack]))
    return max(result)




print(solve("zodiacs"))