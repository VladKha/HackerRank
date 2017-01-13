import itertools


def solve(lists, m):
    result = 0

    for combination in itertools.product(*lists):
        tmp = sum([i ** 2 for i in combination]) % m
        if tmp > result:
            result = tmp

    return result


if __name__ == '__main__':
    k, m = [int(i) for i in input().strip().split(' ')]
    lists = []
    for i in range(k):
        lists.append([int(i) for i in input().strip().split(' ')][1:])
    print(solve(lists, m))
