m = int(input())
s = set(map(int, input().split()))
n = int(input())
t = set(map(int, input().split()))

u = s.symmetric_difference(t)
print(len(u))