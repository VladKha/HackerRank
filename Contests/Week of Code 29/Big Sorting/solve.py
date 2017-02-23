if __name__ == '__main__':
    n = int(input().strip())
    a = [input().strip() for _ in range(n)]

    a.sort(key=int)
    for i in a:
        print(i)
