import collections

if __name__ == '__main__':
    s = input()
    count_map = collections.Counter(s)
    pairs = list(count_map.items())
    pairs.sort(key=lambda pair: (-pair[1], pair[0]))
    for p in pairs[0:3]:
        print(p[0], p[1])
