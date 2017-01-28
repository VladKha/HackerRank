import re

if __name__ == '__main__':
    m = re.search(r'([A-Za-z0-9])\1', input())
    if m:
        print(m.group(1))
    else:
        print(-1)
