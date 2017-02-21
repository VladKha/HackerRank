def check(s):
    if s[0] == '0':
        return False, None

    for first_size in range(1, len(s) // 2 + 1):
        first = s[0:first_size]
        if can_start_from(s, first):
            return True, first

    return False, None


def can_start_from(s, first):
    sequence_length = 1
    v = int(first)
    t = first
    while len(t) < len(s):
        sequence_length += 1
        v += 1
        t += str(v)

    return s == t and sequence_length >= 2


if __name__ == '__main__':
    q = int(input().strip())
    for _ in range(q):
        s = input().strip()

        is_beautiful, start_value = check(s)
        if is_beautiful:
            print('YES', start_value)
        else:
            print('NO')
