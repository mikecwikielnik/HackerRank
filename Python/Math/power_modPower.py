def power_mod1(a, b):
    u = pow(a,b)
    print(u)

def power_mod2(a,b,m):
    v = pow(a,b,m)
    print(v)
    
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    m = int(input())
    result1 = power_mod1(x, y)
    result2 = power_mod2(x, y, m)
