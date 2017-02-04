import re

if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        s = input()
        s = re.sub(r'(?<=\s)&&(?=\s)', r'and', s)
        s = re.sub(r'(?<=\s)\|\|(?=\s)', r'or', s)
        print(s)
