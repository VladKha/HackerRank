import re

if __name__ == '__main__':
    g = int(input())

    for _ in range(g):
        n = int(input())
        s = ''.join(input().split()).strip('1')

        pattern = re.compile(r'1{2,}')
        splits = re.split(pattern=pattern, string=s)

        turns = 0
        for split in splits:
            if len(split) > 2:
                turns += len(split) - 2

        print('Alice' if turns % 2 != 0 else 'Bob')
