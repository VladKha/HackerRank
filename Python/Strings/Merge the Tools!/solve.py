def merge_the_tools(s, k):
    n = len(s)

    result = []
    current = ''
    for i in range(n):
        if s[i] not in current:
            current += s[i]
        if (i + 1) % k == 0:
            result.append(current)
            current = ''

    for i in result:
        print(i)


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
