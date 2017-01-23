import collections

if __name__ == '__main__':
    n = int(input())
    result = collections.OrderedDict()
    for _ in range(n):
        parts = input().split()
        item, price = ' '.join(parts[:-1]), int(parts[-1])
        if item not in result:
            result[item] = 0

        result[item] += price

    for item, price in result.items():
        print(item, price)
