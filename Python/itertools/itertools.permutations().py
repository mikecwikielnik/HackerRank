from itertools import permutations

S, k = input().split()

for x in permutations(sorted(S), int(k)):
    print(*x, sep='')