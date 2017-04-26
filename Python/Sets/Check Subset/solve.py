if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        input()
        a = set(input().split())
        input()
        b = set(input().split())
        print(a.issubset(b))
