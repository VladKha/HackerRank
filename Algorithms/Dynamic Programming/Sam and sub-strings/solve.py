MOD = 10**9+7.


def solve(num):
    n = len(num)
    result = 0

    f = 1
    for i in reversed(range(0, n)):
        result = (result + int(num[i]) * f * (i + 1)) % MOD
        f = (f * 10 + 1) % MOD

    return result

if __name__ == '__main__':
    num = input()
    print(int(solve(num)))
