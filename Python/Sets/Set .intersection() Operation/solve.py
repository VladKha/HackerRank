if __name__ == '__main__':
    input()
    a = set(map(int, input().split()))
    input()
    b = set(map(int, input().split()))
    print(len(a & b))
