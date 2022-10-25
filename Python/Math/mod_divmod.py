from math import trunc


def division_mod(a, b):
    i = a/b
    print(trunc(i))
    j = a%b
    print(j)
    print(divmod(a,b))

    
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    result = division_mod(x, y)