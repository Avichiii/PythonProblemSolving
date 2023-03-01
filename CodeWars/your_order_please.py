import re
def order(sentence):
    sentences = str(sentence)
    # Finding all the digits in the str
    digit_lst = re.findall(r'(\d+)', sentences)
    # Zipping = [('1', 'Thi1s'), ('2', 'is2'), ('3', '3a'), ('4', 'T4est')] + sorting
    sort = sorted(zip(digit_lst, sentences.split()), reverse=False)
    result = []
    for i in sort:
        i = list(i)
        result.append(i[1])
    
    return ' '.join(result)

order("is2 Thi1s T4est 3a")

    