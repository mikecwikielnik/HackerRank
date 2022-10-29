a=set(input().split())
n=int(input())
result=True
for _ in range(n):
    b=set(input().split())
    if not a.issuperset(b):
        result=False
        break
print(result)