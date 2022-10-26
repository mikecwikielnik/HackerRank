def diagonalDifference(arr):
    x = sum([arr[i][i] for i in range(len(arr))])
    y = sum([arr[i][len(arr)-i-1] for i in range(len(arr))])
    z = abs(x - y)
    return z

if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)