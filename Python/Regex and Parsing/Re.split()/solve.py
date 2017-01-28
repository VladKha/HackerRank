import re

if __name__ == '__main__':
    result = re.split(r'[,.]', input())
    for s in result:
        if s.isdigit():
            print(s)
