def miniMaxSum(arr):
    a = sorted(arr)
    b = a[0:4]
    c = a[-4:]
    uSum = 0
    vSum = 0
    
    for u in b:
        uSum = u + uSum


    for v in c:
        vSum = v + vSum

    print(f'{uSum} {vSum}')


if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
