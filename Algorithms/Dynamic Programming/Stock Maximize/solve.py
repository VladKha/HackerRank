def solve():
    n = int(input())
    prices = [int(i) for i in input().split(' ')]

    profit = 0
    max_so_far = 0

    for i in reversed(range(0, n)):
        if prices[i] >= max_so_far:
            max_so_far = prices[i]
        profit += max_so_far - prices[i]

    return profit

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        print(solve())
