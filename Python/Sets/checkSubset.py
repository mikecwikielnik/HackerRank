
n = int(input())
for _ in range(n):
    x = int(input())
    a = set(map(int, input().split()))
    y = int(input())
    b = set(map(int, input().split()))

    if len(a-b) == 0:
        print(True)
    else:
        print(False)

