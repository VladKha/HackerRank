import statistics as st

if __name__ == '__main__':
    n, x = map(int, input().split())
    grades = [list(map(float, input().split())) for _ in range(x)]
    for student_grades in zip(*grades):
        print(st.mean(student_grades))
