m = int(input())
s = set(map(int, input().split()))
n = int(input())
t = set(map(int, input().split()))

u = s.intersection(t)
print(len(u))