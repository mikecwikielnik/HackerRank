m = int(input())
s = set(map(int, input().split()))
n = int(input())
t = set(map(int, input().split()))

u = s.union(t)
print(len(u))