if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        l = [int(s) for s in input().split()]

        a, b = 0, len(l)-1

        tmp = []
        while a <= b:
            if l[a] > l[b]:
                tmp.append(l[a])
                a += 1
            else:
                tmp.append(l[b])
                b -= 1

        if sorted(l, reverse=True) == tmp:
            print('Yes')
        else:
            print('No')
