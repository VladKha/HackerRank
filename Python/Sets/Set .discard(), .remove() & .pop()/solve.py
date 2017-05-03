if __name__ == '__main__':
    input()
    s = set(int(i) for i in input().split())

    n = int(input())
    for _ in range(n):
        a = input().split()
        command = a[0]
        if command == 'pop':
            s.pop()
        elif command == 'remove':
            s.remove(int(a[1]))
        else:
            s.discard(int(a[1]))

    print(sum(s))
