def set_function(a, b):
    k = a.difference(b)
    j = b.difference(a)
    u = list(k)
    v = list(j)
    l = u + v
    m = sorted(l)
    
    for i in m:
        print(i)

if __name__ == '__main__':
    x = int(input())
    x = set(map(int, input().split()))
    y = int(input())
    y = set(map(int, input().split()))
    result = set_function(x, y)