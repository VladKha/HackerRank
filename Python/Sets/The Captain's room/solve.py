if __name__ == '__main__':
    k, a = int(input()), list(map(int, input().split()))
    s = set(a)
    print(((sum(s) * k) - (sum(a))) // (k - 1))
