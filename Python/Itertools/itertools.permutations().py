import itertools


def solve(s, k):
    return sorted(list(itertools.permutations(s, k)))


if __name__ == '__main__':
    input_parts = input().strip().split(' ')
    s, k = input_parts[0], int(input_parts[1])
    for s in solve(s, k):
        print(''.join(i for i in s))
