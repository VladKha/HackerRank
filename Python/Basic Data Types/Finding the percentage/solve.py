if __name__ == '__main__':
    n = int(input())
    d = {}

    for _ in range(n):
        parts = input().split()
        d[parts[0]] = list(map(float, parts[1:]))

    name = input()

    grades = d[name]
    print('{:.2f}'.format(sum(grades) / len(grades)))
