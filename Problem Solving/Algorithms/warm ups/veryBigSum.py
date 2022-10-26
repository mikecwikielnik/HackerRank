def aVeryBigSum(ar):
    sum = 0

    for i in ar:
        sum = i + sum
    
    print(sum)

if __name__ == '__main__':
    ar_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = aVeryBigSum(ar)
