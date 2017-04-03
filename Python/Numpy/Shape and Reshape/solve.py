import numpy as np

if __name__ == '__main__':
    a = np.array(list(map(int, input().split())))
    print(np.reshape(a, (3, 3)))
