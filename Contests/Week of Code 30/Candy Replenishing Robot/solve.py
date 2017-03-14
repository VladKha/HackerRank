if __name__ == '__main__':
    n, t_end = map(int, input().split())
    c = list(map(int, input().split()))

    b = n
    t = 0
    total = 0
    while True:
        b -= c[t]
        if t + 1 == t_end:
            break
        if b < 5:
            to_add = n - b
            b += to_add
            total += to_add
        t += 1

    print(total)
