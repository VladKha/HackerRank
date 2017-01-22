cube = lambda x: x ** 3


def fibonacci(n):
    result = []

    prev, next = 0, 1
    for i in range(n):
        result.append(prev)
        prev, next = next, prev + next

    return result


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
