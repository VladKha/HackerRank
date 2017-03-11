if __name__ == '__main__':
    r, c = map(int, input().split())
    pattern = [
        '..O..',
        'O.o.O',
        '..O..'
    ]

    result = ''

    for i in range(r):
        result += c * pattern[0]
        result += '\n'
        result += c * pattern[1]
        result += '\n'
        result += c * pattern[2]
        result += '\n'

    print(result[:-1])
