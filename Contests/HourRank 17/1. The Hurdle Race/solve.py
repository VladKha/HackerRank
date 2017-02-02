if __name__ == '__main__':
    n, k = map(int, input().split())
    a = map(int, input().split())
    max_height = max(a)
    if k >= max_height:
        print(0)
    else:
        print(max_height - k)
