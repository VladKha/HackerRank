from functools import reduce
from operator import concat


def compare(s):
    if s.islower():
        return ord(s)
    elif s.isupper():
        return ord(s) * 10
    elif int(s) % 2 != 0:
        return ord(s) * 100
    else:
        return ord(s) * 1000

if __name__ == '__main__':
    s = input()
    result = sorted(s, key=compare)
    print(reduce(concat, result))
