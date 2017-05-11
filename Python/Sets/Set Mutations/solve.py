def read_set():
    return set(input().strip().split())

if __name__ == '__main__':
    input()
    a = read_set()
    n = int(input())

    for _ in range(n):
        parts = input().strip().split()
        if parts[0] == 'intersection_update':
            a.intersection_update(read_set())
        elif parts[0] == 'update':
            a.update(read_set())
        elif parts[0] == 'symmetric_difference_update':
            a.symmetric_difference_update(read_set())
        elif parts[0] == 'difference_update':
            a.difference_update(read_set())

    print(sum(map(int, a)))
