import itertools


def solve(a, b):
    return list(itertools.product(a, b))


if __name__ == '__main__':
    a = [int(i) for i in input().strip().split(' ')]
    b = [int(i) for i in input().strip().split(' ')]
    print(' '.join(str(i) for i in solve(a, b)))
