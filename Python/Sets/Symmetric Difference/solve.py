if __name__ == '__main__':
    input()
    a = set(map(int, input().split()))
    input()
    b = set(map(int, input().split()))
    result = (a | b) - (a & b)  # a.symmetric_difference(b), a ^ b
    for e in sorted(result):
        print(e)
