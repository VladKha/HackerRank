import re

if __name__ == '__main__':
    t = int(input())
    pattern = re.compile(r'[+-]?\d*\.\d+')
    for i in range(t):
        print(bool(re.fullmatch(pattern, input())))
