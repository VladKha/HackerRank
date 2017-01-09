def max_subarray(a):
    n = len(a)

    dp = {0: a[0]}
    for i in range(1, n):
        dp[i] = max(dp[i-1]+a[i], a[i])

    return max(dp.values())


def max_subsequence(a):
    result = 0
    max_negative = -float('inf')

    for e in a:
        if e > 0:
            result += e
        else:
            max_negative = max(max_negative, e)

    return result if result > 0 else max_negative


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        _ = input()
        a = [int(j) for j in input().strip().split(' ')]
        print(max_subarray(a), max_subsequence(a))
