import numpy as np

if __name__ == '__main__':
    n, m = map(int, input().split())
    a = np.array([[int(j) for j in input().split()] for i in range(n)])
    b = np.array([[int(j) for j in input().split()] for i in range(n)])

    print(a + b)
    print(a - b)
    print(a * b)
    print(a // b)
    print(a % b)
    print(a ** b)
