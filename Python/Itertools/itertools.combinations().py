import itertools


def solve(s, k):
    result = []

    for i in range(1, k + 1):
        result += list(itertools.combinations(sorted(s), i))

    return result


if __name__ == '__main__':
    input_parts = input().strip().split(' ')
    s, k = input_parts[0], int(input_parts[1])
    for s in solve(s, k):
        print(''.join(i for i in s))
