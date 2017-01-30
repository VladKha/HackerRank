import string


def weight(letter):
    return string.ascii_lowercase.index(letter) + 1

if __name__ == '__main__':
    s = input().strip()
    weights = set()
    tmp = weight(s[0])
    weights.add(tmp)
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            tmp += weight(s[i])
        else:
            tmp = weight(s[i])
        weights.add(tmp)

    n = int(input().strip())
    for i in range(n):
        x = int(input().strip())
        if x in weights:
            print('Yes')
        else:
            print('No')
