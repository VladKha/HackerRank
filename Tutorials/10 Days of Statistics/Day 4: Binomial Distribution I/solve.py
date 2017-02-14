from math import factorial as f


def binomial_dist(x, n, p):
    return f(n) / f(x) / f(n - x) * p ** x * (1 - p) ** (n - x)

if __name__ == '__main__':
    a, b = map(float, input().split())
    p = 1 / (a + b) * a
    n = 6
    x = 3
    print('{:.3f}'.format(sum(binomial_dist(i, n, p) for i in range(x, n + 1))))
