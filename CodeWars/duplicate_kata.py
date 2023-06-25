# function_list = [
#     lambda x: x * 2,
#     lambda x: x ** 2,
#     lambda x: x + 20,
#     lambda x: x / 1000,
#     lambda x: x * x,
#     lambda x: pow(x, 2),
#     lambda x: x % 2
# ]
# list_ = []
# duplicate = []
# for i in range(len(function_list)):
#     s = function_list[i](250)
#     if s in list_:
#         duplicate.append()
#     list_.append(s)
# print(duplicate)

# numbers = range(10)
def dupe_detect(functions):
    
    diction ={}
    
    for fun in range(len(functions)):
        result =''
        for x in range(255):
            result += str(functions[fun](x))
            # print(result)
        if result not in diction:
            diction[result] = [fun]
        else:
            diction[result] += [fun]
    print(diction.values())
    functions = [x for x in diction.values() if len(x) > 1]
    return functions

functions = [
    lambda x: x * 2,
    lambda x: x ** 2,
    lambda x: x + 20,
    lambda x: x / 1000,
    lambda x: x * x,
    lambda x: pow(x, 2),
    lambda x: x % 2
]
print(dupe_detect(functions))