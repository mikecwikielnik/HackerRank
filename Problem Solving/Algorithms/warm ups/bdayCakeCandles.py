def birthdayCakeCandles(candles):
    lg = max(candles)
    l = []

    for i in candles:
        if i == lg:
            l.append(i)
    
    print(len(l))


if __name__ == '__main__':
    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

