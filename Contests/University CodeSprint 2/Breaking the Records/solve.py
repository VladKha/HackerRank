if __name__ == '__main__':
    n = int(input())
    scores = [int(i) for i in input().strip().split()]
    min_score = max_score = scores[0]
    min_breaks = max_breaks = 0
    for i in range(1, n):
        if scores[i] < min_score:
            min_score = scores[i]
            min_breaks += 1
        elif scores[i] > max_score:
            max_score = scores[i]
            max_breaks += 1

    print(max_breaks, min_breaks)
