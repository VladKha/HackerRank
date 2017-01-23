import collections

if __name__ == '__main__':
    n = int(input())
    result = collections.OrderedDict()
    for _ in range(n):
        s = input()

        if s not in result:
            result[s] = 0

        result[s] += 1

    print(len(result))
    print(*result.values())
