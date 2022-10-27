def weightedMean(X, W):
    wsum =0
    for i in range(len(X)):
        wsum += X[i]*W[i]

    print(round(wsum/sum(W),1))

if __name__ == '__main__':
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))

    weights = list(map(int, input().rstrip().split()))

    weightedMean(vals, weights)