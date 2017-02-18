from math import factorial as f


def binomial_dist(x, n, p):
    return f(n) / f(x) / f(n - x) * p ** x * (1 - p) ** (n - x)

if __name__ == '__main__':
    s = input().split()
    p, n = float(s[0]), int(s[1])
    p /= 100
    x = 2
    print('{:.3f}'.format(sum(binomial_dist(i, n, p) for i in range(x + 1))))
    print('{:.3f}'.format(sum(binomial_dist(i, n, p) for i in range(x, n+1))))
