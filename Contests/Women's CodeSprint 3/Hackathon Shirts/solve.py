from collections import Counter

inf = float('inf')


class IntervalTree:
    def __init__(self, intervals):
        self.root = self.construct_tree(intervals=sorted(intervals, key=lambda x: x.get_begin()))

    def construct_tree(self, intervals):
        if not intervals:
            return None

        root_index = len(intervals) // 2
        root = Node(intervals[root_index])
        root.max_right = max(intervals, key=lambda x: x.get_end()).get_end()

        root.left = self.construct_tree(intervals[0:root_index])
        root.right = self.construct_tree(intervals[root_index + 1:])

        return root

    def contains(self, point):
        return self._contains(self.root, point)

    def _contains(self, node, point):
        if node.a() <= point <= node.b():
            return True
        elif node.left is None or node.left.max_right < point:
            if node.right is not None:
                return self._contains(node.right, point)
            else:
                return False
        else:
            return self._contains(node.left, point)


class Interval:
    def __init__(self, begin, end):
        self.begin = begin
        self.end = end

    def get_begin(self):
        return self.begin

    def get_end(self):
        return self.end


class Node:
    def __init__(self, interval: Interval):
        self.interval = interval
        self.max_right = -inf
        self.left = None
        self.right = None

    def a(self):
        return self.interval.get_begin()

    def b(self):
        return self.interval.get_end()

if __name__ == '__main__':
    q = int(input())

    for _ in range(q):
        input()
        sizes = Counter(map(int, input().split()))
        v = int(input())

        vendor_stock = [
            Interval(*list(map(int, input().split()))) for _ in range(v)
        ]

        tree = IntervalTree(vendor_stock)
        counter = 0
        for s, count in sizes.most_common():
            if tree.contains(s):
                counter += count

        print(counter)
