""" DP solution O(n^2) - too long """
# def lis(a):
#     dp = {0: 1}
#     n = len(a)
#     for i in range(1, n):
#         dp[i] = 1
#         for j in range(i):
#             if a[j] < a[i]:
#                 dp[i] = max(dp[i], dp[j] + 1)
#
#     return max(dp.values())


def modified_bin_search(x, a):
    n = len(a)
    s, f = 0, n - 1
    while s < f:
        mid = (s + f) // 2

        if s > f:
            return mid + 1

        if x < a[mid]:
            f = mid - 1
        elif a[mid] < x:
            s = mid + 1
        else:
            return mid


def lis(a):
    n = len(a)
    s = [a[0]]
    for i in range(1, n):
        if s[-1] < a[i]:
            s.append(a[i])
        else:
            index = modified_bin_search(a[i], s)
            s[index] = a[i]

    return len(s)

if __name__ == '__main__':
    n = int(input())
    a = [int(input()) for _ in range(n)]
    print(lis(a))
