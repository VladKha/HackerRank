import numpy as np

if __name__ == '__main__':
    n, m = map(int, input().split())
    a = np.array(
        [list(map(int, input().split())) for _ in range(n)]
    )
    print(np.transpose(a))
    print(a.flatten())
