import collections

if __name__ == '__main__':
    n, m = list(map(int, input().split()))

    d = collections.defaultdict(list)

    for i in range(n):
        d[input()].append(i + 1)

    for i in range(m):
        print(' '.join(map(str, d[input()])) or -1)
