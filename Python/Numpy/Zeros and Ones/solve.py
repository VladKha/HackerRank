import numpy as np

if __name__ == '__main__':
    numbers = list(map(int, input().strip().split()))
    a = np.zeros(numbers, dtype=np.int)
    b = np.ones(numbers, dtype=np.int)

    print(a)
    print(b)
