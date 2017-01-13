import itertools


def solve(s):
    result = []

    for key, group in itertools.groupby(s):
        result.append((len(list(group)), int(key)))

    return result


if __name__ == '__main__':
    s = input()
    print(' '.join(str(i) for i in solve(s)))
