if __name__ == '__main__':
    n = int(input())
    elements = list(map(int, input().split()))
    weights = list(map(int, input().split()))
    print('{:.1f}'.format(sum([elements[i] * weights[i] for i in range(n)]) / sum(weights)))
