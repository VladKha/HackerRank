if __name__ == '__main__':
    q = int(input())
    for _ in range(q):
        n = int(input())
        a = [int(i) for i in input().split()]

        possible = True
        for i in range(n-1):
            if a[i] > a[i+1]:
                if a[i] - a[i+1] == 1:
                    a[i], a[i+1] = a[i+1], a[i]
                else:
                    possible = False
                    break

        print('Yes' if possible else 'No')
