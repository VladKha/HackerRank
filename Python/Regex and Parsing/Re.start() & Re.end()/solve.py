if __name__ == '__main__':
    s = input()
    k = input()
    n = len(k)

    found = False
    for i in range(0, len(s) - n + 1):
        line = s[i:i + n]
        if line == k:
            print('({}, {})'.format(i, i + n - 1))
            found = True

    if not found:
        print('(-1, -1)')
