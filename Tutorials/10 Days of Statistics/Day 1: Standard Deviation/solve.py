import math
import statistics as st

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    print('{:.1f}'.format(math.sqrt(st.variance(a) * (n-1) / n)))
