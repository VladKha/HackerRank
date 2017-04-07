import numpy as np

if __name__ == '__main__':
    n, m, p = map(int, input().split())

    a = [
        list(map(int, input().split())) for _ in range(n)
    ]
    b = [
        list(map(int, input().split())) for _ in range(m)
    ]
    print(np.concatenate((a, b)))
