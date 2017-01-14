import collections

if __name__ == '__main__':
    x = int(input())
    sizes = [int(i) for i in input().strip().split(' ')]
    n = int(input())

    sizes = collections.Counter(sizes)
    result = 0
    for i in range(n):
        size, price = [int(i) for i in input().strip().split(' ')]
        if size in sizes:
            result += price
            if sizes[size] == 1:
                sizes.pop(size)
            else:
                sizes[size] -= 1

    print(result)
