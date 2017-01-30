if __name__ == '__main__':
    n = int(input().strip())
    for i in range(n):
        grade = int(input().strip())
        if grade >= 38:
            next_multiple = (grade // 5 + 1) * 5
            if next_multiple - grade < 3:
                grade = next_multiple
        print(grade)
