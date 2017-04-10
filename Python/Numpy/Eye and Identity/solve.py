import numpy as np

if __name__ == '__main__':
    n, m = map(int, input().split())
    print(np.eye(n, m))
