def geometric_dist(p, n):
    return (1 - p) ** (n - 1) * p

if __name__ == '__main__':
    a, b = map(int, input().strip().split())
    n = int(input().strip())

    p = a / b
    print('{:.3f}'.format(sum(geometric_dist(p, i) for i in range(1, n + 1))))
