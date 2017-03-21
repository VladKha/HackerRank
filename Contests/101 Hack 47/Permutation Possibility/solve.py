from collections import Counter

if __name__ == '__main__':
    m = int(input())
    a = list(map(int, input().split()))
    if len(Counter(a)) == len(a):
        print('YES')
    else:
        print('NO')
