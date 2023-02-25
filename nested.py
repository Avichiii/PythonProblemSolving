#HackerRank
if __name__ == '__main__':
    outer = []
    for _ in range(int(input())):
        inner = []
        name = input()
        score = float(input())
        inner.append(name);inner.append(score)
        outer.append(inner)

    if 2 <= len(outer) <= 5:
        scores = set([elem[1] for elem in outer])
        scores.remove(min(scores))
        second_lowest_min = min(scores)
        sort = []
        for el in outer:
            if el[1] == second_lowest_min:
                sort.append(el[0])
        sort = sorted(sort)
        for i in sort:
            print(i)

'''
    4
    Tina
    52
    Rina
    25
    Mahesh
    26
    Hean
    27
'''

