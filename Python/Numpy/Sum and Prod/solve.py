import numpy as np

if __name__ == '__main__':
    n, m = map(int, input().split())
    a = np.array([
        [int(s) for s in input().split()] for _ in range(n)
    ])
    print(a.sum(axis=0).prod())
