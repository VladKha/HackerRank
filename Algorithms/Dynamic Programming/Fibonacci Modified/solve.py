def fib_modified(t1, t2, n):
    for i in range(n - 1):
        t1, t2 = t2, t1 + t2 ** 2
    return t1


if __name__ == '__main__':
    t1, t2, n = map(int, input().split(' '))
    print(fib_modified(t1, t2, n))
