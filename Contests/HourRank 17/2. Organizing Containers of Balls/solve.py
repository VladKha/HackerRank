if __name__ == '__main__':
    q = int(input())
    for _ in range(q):
        n = int(input())
        sum_row = [0] * n
        sum_column = [0] * n
        for i in range(n):
            row = list(map(int, input().split()))
            for j in range(n):
                sum_row[i] += row[j]
                sum_column[j] += row[j]
        print("Possible" if sorted(sum_row) == sorted(sum_column) else "Impossible")
