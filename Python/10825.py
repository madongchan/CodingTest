import sys
input = sys.stdin.readline
n = int(input().strip())
students = []
for _ in range(n):
    Name, K, E, M = input().strip().split()
    K, E, M = int(K), int(E), int(M)
    students.append((Name, K, E, M)) # 튜플로 수정 X, 한 학생마다 하나의 리스트로 묶음
students.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))
# 정렬된 학생 이름 출력
for student in students:
    print(student[0])
