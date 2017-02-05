import queue as Q
import collections

if __name__ == '__main__':
    n = int(input())
    a = sorted(list(map(int, input().split())))

    # mean
    print('{:.1f}'.format(sum(a) / len(a)))

    # median
    mid = n // 2
    if n % 2 == 0:
        median = (a[mid-1] + a[mid]) / 2
    else:
        median = a[mid]
    print('{:.1f}'.format(median))

    # mode
    count_map = collections.Counter(a)
    q = Q.PriorityQueue()
    for pair in count_map.items():
        q.put((-pair[1], pair[0]))

    print(q.get()[1])
