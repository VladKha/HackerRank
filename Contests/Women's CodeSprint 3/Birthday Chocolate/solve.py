if __name__ == '__main__':
    n = int(input())
    chocolate = list(map(int, input().split()))
    d, m = map(int, input().split())

    result = 0

    for i in range(n - m + 1):
        if sum(chocolate[i:i+m]) == d:
            result += 1

    print(result)
