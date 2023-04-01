from itertools import permutations
par = []
for para in range(4): par.append(para)
print(par)
count = 0
p = permutations(par)
for index in enumerate(p): count+=1
print(count)