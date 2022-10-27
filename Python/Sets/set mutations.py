n = int(input())
s = set(map(int, input().split()))
q = int(input())
for i in range(q):
    w = input().split()     # the logic here is super important. w[0] is also w because w is a one element set -> the strings in the loop!
    t = set(map(int, input().split()))  # we have a big set (s) and a small set (t)
    if w[0] == 'update':
        s.update(t)
    elif w[0] == 'intersection_update':
        s.intersection_update(t)
    elif w[0] == 'difference_update':
        s.difference_update(t)
    elif w[0] == 'symmetric_difference_update':
        s.symmetric_difference_update(t)
print(sum(s))