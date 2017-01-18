if __name__ == '__main__':
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    k = int(input())
    result = sorted(a, key=lambda row: row[k])
    for row in result:
        print(' '.join([str(i) for i in row]))
