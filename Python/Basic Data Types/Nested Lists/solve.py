if __name__ == '__main__':
    n = int(input())
    students = []
    for i in range(n):
        name = input()
        grade = float(input())
        students.append([name, grade])

    students.sort(key=lambda s: (s[1], s[0]))

    first_lowest = students[0][1]
    for s in students:
        if s[1] != first_lowest:
            second_lowest = s[1]
            break

    for s in students:
        if s[1] == second_lowest:
            print(s[0])
