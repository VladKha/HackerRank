if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    a = sorted(a)

    if n % 2 == 0:
        Q2 = (a[n // 2 - 1] + a[n // 2]) // 2
        if n % 4 == 0:
            Q1 = (a[n // 4 - 1] + a[n // 4]) // 2
            Q3 = (a[3 * n // 4 - 1] + a[3 * n // 4]) // 2
        else:
            Q1 = a[n // 4]
            Q3 = a[3 * n // 4]
    else:
        Q2 = a[n // 2]
        if (n - 1) % 4 == 0:
            Q1 = (a[n // 4 - 1] + a[n // 4]) // 2
            Q3 = (a[3 * n // 4] + a[3 * n // 4 + 1]) // 2
        else:
            Q1 = a[n // 4]
            Q3 = a[3 * n // 4]

    print(Q1)
    print(Q2)
    print(Q3)
