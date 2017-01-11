def solve(arr, set1, set2):
    result = 0

    for e in arr:
        if e in set1:
            result += 1

    for e in arr:
        if e in set2:
            result -= 1

    return result

if __name__ == '__main__':
    input()
    arr = [int(i) for i in input().split(' ')]
    set1 = set(int(i) for i in input().split(' '))
    set2 = set(int(i) for i in input().split(' '))
    print(solve(arr, set1, set2))
