import itertools


def solve(letters, k):
    combinations = list(itertools.combinations(letters, k))
    with_one_a = list(filter(lambda c: 'a' in c, combinations))
    return len(with_one_a) / len(combinations)

if __name__ == '__main__':
    _, letters, k = input(), [i for i in input().strip().split(' ')], int(input())
    p = solve(letters, k)
    print('{:.4f}'.format(p))
