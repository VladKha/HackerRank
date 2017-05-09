import numpy as np

if __name__ == '__main__':
    a = np.array([
        float(s) for s in input().split()
    ])
    print(np.floor(a))
    print(np.ceil(a))
    print(np.rint(a))
