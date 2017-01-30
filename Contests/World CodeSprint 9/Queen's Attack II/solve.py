def bin_search(square_list, block_square, reverse=False):
    a, b = 0, len(square_list) - 1

    if not reverse:
        while a <= b:
            mid = (a + b) // 2
            if block_square < square_list[mid]:
                b = mid - 1
            elif block_square > square_list[mid]:
                a = mid + 1
            else:
                return mid
    else:
        while a <= b:
            mid = (a + b) // 2
            if block_square > square_list[mid]:
                b = mid - 1
            elif block_square < square_list[mid]:
                a = mid + 1
            else:
                return mid

    raise ValueError

if __name__ == '__main__':
    n, k = map(int, input().strip().split())
    r_q, c_q = map(int, input().strip().split())
    open_squares = {
        'left': [],
        'left-top': [],
        'top': [],
        'right-top': [],
        'right': [],
        'right-bottom': [],
        'bottom': [],
        'left-bottom': []
    }

    # left
    r, c = r_q, c_q
    while c > 1:
        c -= 1
        open_squares['left'].append((r, c))

    # left-top
    r, c = r_q, c_q
    while c > 1 and r < n:
        c -= 1
        r += 1
        open_squares['left-top'].append((r, c))

    # top
    r, c = r_q, c_q
    while r < n:
        r += 1
        open_squares['top'].append((r, c))

    # right-top
    r, c = r_q, c_q
    while c < n and r < n:
        c += 1
        r += 1
        open_squares['right-top'].append((r, c))

    # right
    r, c = r_q, c_q
    while c < n:
        c += 1
        open_squares['right'].append((r, c))

    # right-bottom
    r, c = r_q, c_q
    while c < n and r > 1:
        c += 1
        r -= 1
        open_squares['right-bottom'].append((r, c))

    # bottom
    r, c = r_q, c_q
    while r > 1:
        r -= 1
        open_squares['bottom'].append((r, c))

    # left-bottom
    r, c = r_q, c_q
    while c > 1 and r > 1:
        c -= 1
        r -= 1
        open_squares['left-bottom'].append((r, c))

    # read blocked squares
    for i in range(k):
        r_o, c_o = map(int, input().strip().split())
        direction = ''
        if c_o < c_q:
            direction = 'left'
        elif c_o > c_q:
            direction = 'right'

        diagonal = False
        if r_o > r_q:
            if direction == '':
                direction = 'top'
            else:
                direction += '-top'
                diagonal = True
        elif r_o < r_q:
            if direction == '':
                direction = 'bottom'
            else:
                direction += '-bottom'
                diagonal = True

        if diagonal:
            if abs(r_o - r_q) != abs(c_o - c_q):
                continue

        try:
            # index = open_squares[direction].index((r_o, c_o))     # passed even without binary search
            if direction in ['top', 'right', 'top-right']:
                index = bin_search(open_squares[direction], (r_o, c_o))
            elif direction in ['left', 'bottom', 'left-bottom']:
                index = bin_search(open_squares[direction], (r_o, c_o), reverse=True)
            else:
                index = open_squares[direction].index((r_o, c_o))
            open_squares[direction] = open_squares[direction][0:index]
        except ValueError:
            pass

    result = 0
    for direction, squares in open_squares.items():
        result += len(squares)
    print(result)
