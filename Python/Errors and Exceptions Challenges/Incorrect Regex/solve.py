import re

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        try:
            re.compile(input())
            print(True)
        except:
            print(False)
