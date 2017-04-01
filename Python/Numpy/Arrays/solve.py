import numpy as np

if __name__ == '__main__':
    a = list(map(float, input().split()))
    a = np.array(a)
    print(a[::-1])
