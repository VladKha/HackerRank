if __name__ == '__main__':
    n = int(input())
    a = set(int(i) for i in input().split())
    a = sorted(list(a))
    print(a[-2])
