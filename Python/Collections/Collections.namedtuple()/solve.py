from collections import namedtuple
n = int(input())
Student = namedtuple('Student', input().strip())
students = [Student(*input().strip().split()) for _ in range(n)]
print(sum(int(s.MARKS) for s in students) / n)
