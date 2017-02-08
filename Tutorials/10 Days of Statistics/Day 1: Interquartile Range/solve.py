if __name__ == '__main__':
    def get(i):
        counter = 0
        j = 0
        while True:
            x, f = pairs[j]
            if counter + f <= i:
                counter += f
                j += 1
            elif counter + f > i:
                return x

    def interquantile_range(n):
        if n % 2 == 0:
            if n % 4 == 0:
                q1 = (get(n // 4 - 1) + get(n // 4)) / 2
                q3 = (get(3 * n // 4 - 1) + get(3 * n // 4)) / 2
            else:
                q1 = get(n // 4)
                q3 = get(3 * n // 4)
        else:
            if (n - 1) % 4 == 0:
                q1 = (get(n // 4 - 1) + get(n // 4)) / 2
                q3 = (get(3 * n // 4) + get(3 * n // 4 + 1)) / 2
            else:
                q1 = get(n // 4)
                q3 = get(3 * n // 4)

        return q3 - q1


    n = int(input())
    x = list(map(int, input().split()))
    f = list(map(int, input().split()))
    pairs = sorted(zip(x, f))
    print('{:.1f}'.format(interquantile_range(sum(f))))
