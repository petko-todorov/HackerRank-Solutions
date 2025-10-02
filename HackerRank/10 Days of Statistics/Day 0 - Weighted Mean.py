def weighted_mean(x, w):
    # x[i] * y[i] + x[i+1] * y[i+1] ...
    # ----------------
    # sum(w)
    X, W = [], []

    for i, j in zip(x, w):
        X.append(i * j)
        W.append(j)

    print(round(sum(X) / sum(W), 1))


if __name__ == '__main__':
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))

    weights = list(map(int, input().rstrip().split()))

    weighted_mean(vals, weights)
